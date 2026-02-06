#!/usr/bin/env python3
"""Build Meridian-styled taster documents from Markdown + Mermaid.

Outputs:
- out/tasters/<slug>.docx
- out/tasters/<slug>.pdf (optional)

Design goals:
- Uses Meridian typography + header/footer via scripts/meridian_docx.py helpers.
- Renders Mermaid blocks to PNG and embeds them.
- Keeps content concise and shareable for outreach.

Usage:
  uv sync
  uv run python scripts/build_taster_docs.py --pdf
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import textwrap
from dataclasses import dataclass
from pathlib import Path

import meridian_docx


RE_MERMAID_FENCE = re.compile(r"```mermaid\s*(.*?)\s*```", re.DOTALL)
RE_NUMBERED = re.compile(r"^(\d+)\.\s+(.*)$")


@dataclass(frozen=True)
class TasterSpec:
    slug: str
    title: str
    overline: str
    source_md: Path


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def _render_mermaid_to_png(*, mermaid_code: str, out_png: Path) -> None:
    tmp_mmd = out_png.with_suffix(".mmd")
    tmp_mmd.write_text(mermaid_code.strip() + "\n", encoding="utf-8")

    # Use mermaid-cli via npx (no repo install required).
    cmd = [
        "npx",
        "-y",
        "@mermaid-js/mermaid-cli@latest",
        "-i",
        str(tmp_mmd),
        "-o",
        str(out_png),
        "--backgroundColor",
        "white",
        "--width",
        "1200",
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def _md_to_docx(
    *,
    spec: TasterSpec,
    out_docx: Path,
    out_pdf: Path | None,
    confidentiality: str,
) -> None:
    md = _read_text(spec.source_md)

    # Start a Meridian-styled doc.
    doc = meridian_docx.Document()
    meridian_docx.apply_document_setup(doc, paper="a4")
    meridian_docx.apply_typography(doc)
    meridian_docx.apply_header_footer_tri_footer(
        doc,
        brand_left="Meridian",
        header_right=spec.title,
        footer_left="meridian.health",
        footer_right="Confidential",
        different_first_page=True,
    )

    meridian_docx.add_title_page(
        doc,
        overline=spec.overline,
        title=spec.title,
        date_str=f"{dt.date.today().day} {dt.date.today().strftime('%B %Y')}",
        confidentiality=confidentiality,
    )

    # Parse line-by-line and render:
    # - # Heading -> Heading 1
    # - ## Heading -> Heading 2
    # - ### Heading -> Heading 3
    # - mermaid fences -> image
    # - bullet lines -> list
    # - paragraphs -> Normal

    # Extract mermaid blocks first, replacing them with placeholders.
    mermaid_blocks: list[str] = []

    def _replace_mermaid(match: re.Match[str]) -> str:
        mermaid_blocks.append(match.group(1))
        return f"[[MERMAID:{len(mermaid_blocks) - 1}]]"

    md = RE_MERMAID_FENCE.sub(_replace_mermaid, md)

    lines = md.splitlines()

    section = doc.sections[0]
    usable_width = section.page_width - section.left_margin - section.right_margin

    seen_nonempty = False
    paragraph_lines: list[str] = []

    def _flush_paragraph() -> None:
        if not paragraph_lines:
            return
        doc.add_paragraph(" ".join(paragraph_lines).strip())
        paragraph_lines.clear()

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            _flush_paragraph()
            continue

        # Ignore simple metadata lines (we already include on title page).
        if line.startswith("Audience:") or line.startswith("Status:"):
            continue

        # If the markdown begins with an H1, treat it as the document title
        # (the title page already includes the title).
        if not seen_nonempty and line.startswith("# "):
            seen_nonempty = True
            continue

        seen_nonempty = True

        mermaid_marker = re.match(r"\[\[MERMAID:(\d+)\]\]", line.strip())
        if mermaid_marker:
            _flush_paragraph()
            idx = int(mermaid_marker.group(1))
            out_png = out_docx.parent / "assets" / f"{spec.slug}-diagram-{idx+1}.png"
            _ensure_dir(out_png.parent)
            _render_mermaid_to_png(mermaid_code=mermaid_blocks[idx], out_png=out_png)

            doc.add_picture(str(out_png), width=usable_width)
            continue

        if line.startswith("# "):
            _flush_paragraph()
            doc.add_heading(line[2:].strip(), level=1)
            continue
        if line.startswith("## "):
            _flush_paragraph()
            doc.add_heading(line[3:].strip(), level=2)
            continue
        if line.startswith("### "):
            _flush_paragraph()
            doc.add_heading(line[4:].strip(), level=3)
            continue

        if line.startswith("- "):
            _flush_paragraph()
            # Word list styles vary; use built-in "List Bullet" when available.
            try:
                p = doc.add_paragraph(style="List Bullet")
            except KeyError:
                p = doc.add_paragraph()
            p.add_run(line[2:].strip())
            continue

        numbered = RE_NUMBERED.match(line)
        if numbered:
            _flush_paragraph()
            try:
                p = doc.add_paragraph(style="List Number")
            except KeyError:
                p = doc.add_paragraph()
            p.add_run(numbered.group(2).strip())
            continue

        paragraph_lines.append(textwrap.dedent(line).strip())

    _flush_paragraph()

    out_docx.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out_docx)
    if out_pdf is not None:
        meridian_docx.convert_docx_to_pdf(out_docx, out_pdf=out_pdf)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pdf",
        action="store_true",
        help="Also convert each .docx to PDF via LibreOffice",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    tast_dir = root / "roadmap" / "outreach" / "tasters"
    out_dir = root / "out" / "tasters"
    _ensure_dir(out_dir)

    confidentiality = "Confidential — For internal and approved partner use only"

    specs = [
        TasterSpec(
            slug="theatre-cancellations",
            title="Theatre utilisation & cancellations — 4–6 week pilot",
            overline="Pilot taster",
            source_md=tast_dir / "theatre-cancellations.md",
        ),
        TasterSpec(
            slug="outpatient-dnas",
            title="Outpatients DNAs — 4–6 week pilot",
            overline="Pilot taster",
            source_md=tast_dir / "outpatient-dnas.md",
        ),
        TasterSpec(
            slug="radiology-ops",
            title="Radiology ops & QA workflow — 4–6 week pilot",
            overline="Pilot taster",
            source_md=tast_dir / "radiology-ops.md",
        ),
        TasterSpec(
            slug="nursing-admin",
            title="Nursing documentation/admin burden — 4–6 week pilot",
            overline="Pilot taster",
            source_md=tast_dir / "nursing-admin.md",
        ),
    ]

    for spec in specs:
        out_docx = out_dir / f"{spec.slug}.docx"
        out_pdf = out_dir / f"{spec.slug}.pdf" if args.pdf else None
        _md_to_docx(
            spec=spec,
            out_docx=out_docx,
            out_pdf=out_pdf,
            confidentiality=confidentiality,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
