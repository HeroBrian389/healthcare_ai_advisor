# Pilot taster documents

These are short, shareable “taster” briefs for common hospital wedges.

They’re designed to be attached to outreach emails so prospects can quickly see:

- what the pilot would *actually* do,
- how you’ll handle safety/governance,
- what data is (and isn’t) needed,
- what success looks like.

## Generate styled PDF/DOCX

These Markdown files include Mermaid diagrams. Use the generator to produce Meridian‑styled `.docx` (and optional `.pdf`) with diagrams rendered as images.

```bash
uv sync
uv run python scripts/build_taster_docs.py --pdf
```

Outputs go to `out/tasters/`.

## Notes

- Numbers in charts are **illustrative placeholders**.
- Keep pilots **low risk** by default: start with operational metadata; avoid patient notes unless explicitly agreed.

