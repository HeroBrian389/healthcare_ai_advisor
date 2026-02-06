# Meridian — Brand Design Guidelines

> **Repo tooling:** Use `uv` only for Python. Examples: `uv add <dep>`, `uv sync`, `uv run python <script.py>`.
> Document templates: `uv run python scripts/meridian_docx.py --out out/<name>.docx --pdf`.

**Nordic Slate Design System · Version 1.0 · February 2026**
*Confidential — For internal and approved partner use only*

---

## Contents

1. [Brand Overview](#1-brand-overview)
2. [Colour System](#2-colour-system)
3. [Typography](#3-typography)
4. [Logo & Wordmark](#4-logo--wordmark)
5. [Spacing & Layout](#5-spacing--layout)
6. [Iconography & Visual Elements](#6-iconography--visual-elements)
7. [Photography & Imagery](#7-photography--imagery)
8. [UI Components](#8-ui-components)
9. [Motion & Animation](#9-motion--animation)
10. [Voice & Tone](#10-voice--tone)
11. [Applications](#11-applications)
12. [Accessibility](#12-accessibility)
13. [Don'ts & Common Mistakes](#13-donts--common-mistakes)

---

## 1. Brand Overview

### 1.1 Brand Story

Meridian exists at the intersection of deep clinical understanding and technical excellence. Founded by practitioners who have spent years inside the healthcare system, we bring a rare combination of domain expertise and AI engineering capability to healthcare organisations ready to modernise their clinical workflows.

Our brand must communicate three things simultaneously: **clinical credibility**, **technical sophistication**, and **human warmth**. We are not a generic technology vendor. We are clinician-adjacent problem solvers who happen to build with AI.

### 1.2 Positioning Statement

> For healthcare organisations seeking to integrate AI into clinical workflows, Meridian is the consultancy that combines hands-on clinical experience with deep technical capability, delivering systems that clinicians actually want to use.

### 1.3 Brand Pillars

| Pillar | Meaning |
|---|---|
| **Clinical Credibility** | We understand healthcare because we've been inside it |
| **Technical Depth** | We build production-grade AI systems, not prototypes |
| **Measured Confidence** | We let the work speak — no hype, no jargon for jargon's sake |
| **Human-Centred Design** | Every system we build starts with the clinician's lived experience |

### 1.4 Brand Personality

Meridian speaks like a **senior clinician who also happens to write beautiful code** — authoritative without being arrogant, precise without being cold, warm without being casual.

| We are | We are not |
|---|---|
| Authoritative | Pompous |
| Precise | Pedantic |
| Warm | Casual or familiar |
| Confident | Boastful |
| Understated | Invisible |
| Thoughtful | Slow or indecisive |
| Modern | Trendy or gimmicky |

### 1.5 Design Philosophy — "Nordic Slate"

Our visual identity is named **Nordic Slate** — inspired by the restraint and material honesty of Scandinavian design, the permanence of natural stone, and the quiet authority of well-set serif typography. Every design decision should feel considered, never decorative for its own sake. If an element doesn't earn its place, remove it.

**Guiding principles:**

1. **Restraint over decoration** — Use the minimum visual elements necessary to communicate clearly.
2. **Material honesty** — Colours, textures, and type should feel grounded in real-world materials — stone, paper, ink.
3. **Earned attention** — Emphasis is reserved for what truly matters. If everything is bold, nothing is.
4. **Quiet confidence** — The design should communicate authority through craft, not volume.

---

## 2. Colour System

### 2.1 Primary Palette

These are the core colours used in every Meridian touchpoint. The palette is intentionally restrained — most compositions should use only 3–4 colours from this set.

| Role | Name | Hex | RGB | Usage |
|---|---|---|---|---|
| **Primary Text** | Charcoal | `#2B2D32` | 43, 45, 50 | Headlines, body text, primary UI elements |
| **Secondary Text** | Charcoal Light | `#3E4048` | 62, 64, 72 | Subheadings, secondary content |
| **Brand Accent** | Forest Green | `#3D6B5E` | 61, 107, 94 | CTAs, links, accent elements, brand marks |
| **Accent Light** | Sage | `#4D8272` | 77, 130, 114 | Hover states, secondary accents, illustrations |
| **Background** | Stone | `#F4F3F0` | 244, 243, 240 | Primary page background |
| **Surface** | White | `#FFFFFF` | 255, 255, 255 | Cards, modals, elevated surfaces |
| **Muted Text** | Warm Grey | `#6E7074` | 110, 112, 116 | Captions, metadata, helper text |

### 2.2 Extended Palette

| Role | Name | Hex | RGB | Usage |
|---|---|---|---|---|
| Stone Dark | `#EAEAE6` | 234, 234, 230 | Dividers, subtle backgrounds, alternating table rows |
| Green Pale | `#E8F0ED` | 232, 240, 237 | Success backgrounds, subtle green tints, tag fills |
| Border | `#D4D3D0` | 212, 211, 208 | Borders, separators, input outlines |
| Border Light | `#E8E7E4` | 232, 231, 228 | Card borders, light separators |

### 2.3 Semantic Colours

Used sparingly and only in functional UI contexts (forms, alerts, status indicators).

| Role | Name | Hex | Usage |
|---|---|---|---|
| Success | Forest Green | `#3D6B5E` | Confirmation, positive status, checkmarks |
| Warning | Warm Amber | `#B08A40` | Caution states, pending items |
| Error | Muted Red | `#B04040` | Errors, destructive actions, required fields |
| Info | Charcoal Light | `#3E4048` | Informational banners, tooltips |

### 2.4 Colour Usage Rules

1. **The 70/20/10 rule applies.** ~70% Stone/White backgrounds, ~20% Charcoal text and structural elements, ~10% Forest Green accents.
2. **Never use Forest Green for large background fills.** It is an accent colour — it should draw the eye to small, important elements (buttons, links, labels, data points).
3. **Dark backgrounds are permitted** in hero sections and CTAs using `#2B2D32` (Charcoal) or the gradient `linear-gradient(165deg, #2B2D32 0%, #3E4048 40%, #505460 100%)`. Stone (`#F4F3F0`) becomes the text colour in these contexts.
4. **Never use pure black** (`#000000`). Always use Charcoal (`#2B2D32`) or darker.
5. **Never use pure white text on Forest Green backgrounds.** The contrast ratio is insufficient. Use on Charcoal backgrounds instead.
6. **Coloured text is reserved for Forest Green only.** Never colour body text in Warm Amber, Muted Red, or any non-palette colour.
7. **Opacity** — If you need a lighter variant, use the Extended Palette rather than reducing opacity. Transparent colours render inconsistently across surfaces.

### 2.5 Dark Mode Mapping

| Light Mode | Dark Mode Equivalent |
|---|---|
| Stone `#F4F3F0` (background) | `#1A1A1E` |
| White `#FFFFFF` (surface) | `#242428` |
| Charcoal `#2B2D32` (text) | `#E8E7E4` |
| Forest Green `#3D6B5E` (accent) | `#5AA08C` (lightened for contrast) |
| Border `#D4D3D0` | `#3A3A3E` |
| Muted Text `#6E7074` | `#9A9A9E` |

---

## 3. Typography

### 3.1 Type System

Meridian uses a deliberate serif + sans-serif pairing that signals authority and readability simultaneously.

| Role | Typeface | Weight(s) | Fallback Stack |
|---|---|---|---|
| **Display / Headlines** | Libre Baskerville | Regular (400), Bold (700) | Georgia, "Times New Roman", serif |
| **Body / UI** | Karla | Light (300), Regular (400), Medium (500), SemiBold (600), Bold (700) | system-ui, -apple-system, "Segoe UI", sans-serif |
| **Monospace / Code** | IBM Plex Mono | Regular (400), Medium (500) | "Courier New", monospace |

**Why this pairing works:** Libre Baskerville provides the gravitas and seriousness of a traditional serif — it reads as institutional, credible, and established. Karla is a humanist sans-serif with slightly rounded terminals, adding warmth and approachability to body text and UI elements. Together, they balance authority with accessibility.

### 3.2 Type Scale

Based on a 1.250 ratio (Major Third) with a 16px base.

| Token | Size (px) | Size (rem) | Line Height | Typeface | Weight | Usage |
|---|---|---|---|---|---|---|
| `display-xl` | 56 | 3.5 | 1.05 | Libre Baskerville | 400 | Hero headlines (landing pages only) |
| `display-lg` | 44 | 2.75 | 1.08 | Libre Baskerville | 400 | Page titles |
| `display-md` | 36 | 2.25 | 1.12 | Libre Baskerville | 400 | Section headings |
| `heading-lg` | 28 | 1.75 | 1.2 | Libre Baskerville | 400 | Subsection headings |
| `heading-md` | 22 | 1.375 | 1.3 | Karla | 600 | Card titles, feature names |
| `heading-sm` | 18 | 1.125 | 1.35 | Karla | 600 | Small headings, labels |
| `body-lg` | 17 | 1.0625 | 1.7 | Karla | 400 | Lead paragraphs, introductions |
| `body` | 15 | 0.9375 | 1.65 | Karla | 400 | Standard body text |
| `body-sm` | 13 | 0.8125 | 1.55 | Karla | 400 | Captions, metadata, helper text |
| `label` | 12 | 0.75 | 1.4 | Karla | 600 | Overline labels, tags, uppercase micro-text |
| `code` | 14 | 0.875 | 1.5 | IBM Plex Mono | 400 | Code snippets, technical references |

### 3.3 Heading Rules

- **Libre Baskerville headings should always be `font-weight: 400` (Regular).** The natural stroke contrast of the serif provides emphasis. Bold Baskerville is reserved for rare cases inside body text.
- **Karla headings use SemiBold (600),** never Bold (700) — this maintains the restrained feel.
- **Letter-spacing:** Libre Baskerville display sizes (`display-xl`, `display-lg`) should use `-0.03em` tracking. Karla headings use default tracking. Uppercase labels use `+0.08em` to `+0.1em` tracking.
- **Headings never use Forest Green.** They are always Charcoal (`#2B2D32`). Green is reserved for accent labels and interactive elements.
- **Never apply italic to Libre Baskerville headings.** Italic Baskerville is permitted only for pull quotes and editorial emphasis.

### 3.4 Body Text Rules

- **Default body text:** 15px / Karla Regular / `#2B2D32` / line-height 1.65.
- **Maximum line length:** 65–75 characters (approximately 680px at 15px). Wider lines are harder to read.
- **Paragraph spacing:** Use `margin-bottom` equal to one line-height (approximately 24px). Never use double line breaks.
- **Bold in body text:** Use Karla SemiBold (600). Never use Bold (700) in body text — it disrupts the quiet tone.
- **Links in body text:** Forest Green (`#3D6B5E`), no underline by default, underline on hover. Never use blue for links.
- **Lists:** Use Karla Regular. Bullet character is a mid-dot (`·`) or simple disc. Numbered lists use Karla Medium. Indent lists at 24px.

### 3.5 Overline Labels

Overline labels are small, uppercase, tracked-out text used to categorise sections. They are a signature Meridian pattern.

```
Font:       Karla SemiBold (600)
Size:       12px
Transform:  uppercase
Tracking:   +0.08em to +0.1em
Colour:     Forest Green (#3D6B5E)
```

**Examples:** `SERVICES`, `CASE STUDY`, `HEALTHCARE AI CONSULTANCY`, `ABOUT US`

### 3.6 Pull Quotes & Callouts

```
Font:       Libre Baskerville Italic
Size:       22–28px
Colour:     Charcoal (#2B2D32)
Border:     2px left border in Forest Green
Padding:    24px left
```

### 3.7 Font Loading

- Load Libre Baskerville and Karla from Google Fonts.
- Use `font-display: swap` to prevent invisible text during loading.
- Subset to Latin and Latin Extended if performance is a concern.
- **Never substitute with Inter, Roboto, or Arial.** If Google Fonts is unavailable, fall back to Georgia + system-ui.

---

## 4. Logo & Wordmark

### 4.1 Primary Logo

The Meridian logo is a **wordmark** — the company name set in Libre Baskerville Regular with a custom square mark. There is no abstract symbol. The wordmark is the logo.

**Wordmark specification:**
- Typeface: Libre Baskerville Regular
- Tracking: `-0.02em`
- Colour: Charcoal (`#2B2D32`) on light backgrounds, Stone (`#F4F3F0`) on dark backgrounds

**Square mark:**
- A 36×36px (scalable) rounded rectangle (border-radius: 8px at 36px)
- Filled with a gradient: `linear-gradient(135deg, #3D6B5E, #4D8272)`
- Contains a white "M" set in Libre Baskerville Bold, centred
- Gap between mark and wordmark: 12px at default scale

### 4.2 Logo Variants

| Variant | Use Case |
|---|---|
| **Full lockup** (mark + wordmark) | Primary usage. Website header, documents, presentations. |
| **Mark only** | Favicons, app icons, social media avatars, small spaces below 120px width. |
| **Wordmark only** | Formal documents, legal contexts, co-branding where the mark is too small. |
| **Reversed** | On Charcoal or dark photographic backgrounds. Mark gradient remains; wordmark becomes Stone. |

### 4.3 Clear Space

Minimum clear space around the full logo lockup is equal to the **height of the capital "M" in the wordmark** on all sides. No other text, graphic, or element may enter this zone.

### 4.4 Minimum Sizes

| Variant | Minimum Width |
|---|---|
| Full lockup | 120px (digital), 30mm (print) |
| Mark only | 24px (digital), 8mm (print) |
| Wordmark only | 100px (digital), 25mm (print) |

### 4.5 Logo Misuse

Do not:
- Change the logo colours to anything outside the approved palette
- Add drop shadows, outlines, glows, or 3D effects
- Stretch, compress, rotate, or skew the logo
- Place the logo on busy or low-contrast backgrounds without a container
- Rearrange the mark and wordmark relative positions
- Recreate the wordmark in a different typeface
- Add a tagline inside the clear space zone
- Animate the logo (the mark may be animated independently — see Motion section)

---

## 5. Spacing & Layout

### 5.1 Spacing Scale

All spacing is based on multiples of **4px** with a core unit of **8px**.

| Token | Value | Usage |
|---|---|---|
| `space-1` | 4px | Tight internal padding (icon-to-text gap) |
| `space-2` | 8px | Default internal padding |
| `space-3` | 12px | Small component gaps |
| `space-4` | 16px | Standard component gaps, form element spacing |
| `space-6` | 24px | Paragraph spacing, card padding |
| `space-8` | 32px | Section sub-padding |
| `space-10` | 40px | Section heading to content |
| `space-12` | 48px | Between content sections on a page |
| `space-16` | 64px | Major section breaks |
| `space-20` | 80px | Top-level page sections |
| `space-24` | 96px | Hero section padding |

### 5.2 Layout Grid

**Desktop (≥1024px):**
- Max content width: **1200px**, centred
- Horizontal padding: 48px each side
- 12-column grid, 16px gutters
- Primary content: 8 columns (max ~680px for text)
- Sidebar/secondary content: 4 columns

**Tablet (768–1023px):**
- Horizontal padding: 32px
- 8-column grid, 16px gutters
- Full-width content blocks

**Mobile (<768px):**
- Horizontal padding: 20px
- Single column
- Stack all content vertically

### 5.3 Content Width Rules

- **Body text** must never exceed 680px width (approximately 65–75 characters per line).
- **Full-width elements** (hero sections, CTA banners, stat bars) may span the full 1200px.
- **Cards in a grid** use 3 columns on desktop, 2 on tablet, 1 on mobile.
- **Tables** may exceed the body text width up to the full content width (1200px) when data requires it.

### 5.4 Vertical Rhythm

All vertical spacing should feel rhythmic and predictable:

- Between sections: `space-20` (80px)
- Between subsections: `space-12` (48px)
- Section label to heading: `space-3` (12px)
- Heading to first paragraph: `space-6` (24px)
- Between paragraphs: `space-6` (24px)
- Between list items: `space-2` (8px)

---

## 6. Iconography & Visual Elements

### 6.1 Icon Style

Meridian uses **outline-style icons** with the following specifications:

| Property | Value |
|---|---|
| Stroke weight | 1.5px |
| Corner radius | 2px (rounded joins) |
| Style | Outline only, never filled |
| Colour | Charcoal (`#2B2D32`) default; Forest Green (`#3D6B5E`) for interactive/accent |
| Sizes | 16px (inline), 20px (buttons), 24px (standalone), 32px (feature icons) |

**Recommended icon set:** Lucide Icons (open source, consistent with our stroke weight and style). Phosphor Icons (light weight) is an acceptable alternative.

**Never use:** Filled/solid icon styles, emoji as UI icons, custom illustrations where a standard icon suffices, Font Awesome (too heavy, inconsistent stroke weights).

### 6.2 Numbered Service Items

Services and process steps use a signature numbered pattern:

```
Number:     Libre Baskerville, 14px, Forest Green, SemiBold
            Formatted as "01", "02", "03" etc.
Title:      Libre Baskerville, 24px, Charcoal, Regular
Body:       Karla, 15px, Warm Grey, Regular
Layout:     Number left-aligned (32px wide), content to the right
Divider:    1px Border colour below each item
```

### 6.3 Dividers & Lines

- **Standard divider:** 1px solid `#D4D3D0` (Border)
- **Subtle divider:** 1px solid `#E8E7E4` (Border Light) — for use inside cards or between closely related items
- **Accent divider:** 2px solid `#3D6B5E` (Forest Green) — used sparingly, e.g. pull quote left borders, active navigation indicators
- **Section dividers** span the full content width. Card dividers span the card width minus padding.
- **Never use dashed or dotted lines.** Solid only.

### 6.4 Decorative Elements

Meridian's visual language is deliberately minimal, but the following decorative patterns are approved:

**Subtle vertical lines** — Used in dark hero/CTA sections as atmospheric elements. Thin (1px) white lines at 2–4% opacity, spaced 120px apart, with a vertical gradient fade (transparent → visible → transparent).

**Overline accent dots** — A 6px circle in Forest Green used to the left of overline labels. Adds visual anchoring without clutter.

**Status indicator dots** — 6–8px circles used in dashboards and status displays. Use semantic colours only.

**Do not use:** Gradients as decorative backgrounds (except in the approved dark hero pattern), geometric shapes, decorative illustrations, background patterns, halftone effects, or any element that doesn't serve a functional purpose.

---

## 7. Photography & Imagery

### 7.1 Photography Style

Meridian's photography should feel **documentary, not staged**. We photograph real clinical environments, real technology, and real moments of collaboration.

**Mood:** Warm, natural light. Calm. Focused. Never clinical-cold, never stock-photo-bright.

| Do | Don't |
|---|---|
| Natural light, slightly warm white balance | Fluorescent / flat / overlit |
| Real clinical environments (with permission) | Generic stock photos of stethoscopes |
| Candid moments of concentration or collaboration | Posed smiling-at-camera shots |
| Clean, uncluttered compositions | Busy, cluttered backgrounds |
| People of diverse backgrounds working naturally | Models in white coats holding clipboards |
| Desaturated slightly toward our warm palette | Oversaturated, HDR, or heavy filters |

### 7.2 Image Treatment

- **Default treatment:** No overlay. Images are used at natural exposure with a slight warmth adjustment to harmonise with the Stone palette.
- **Text overlay treatment:** When text must sit over an image, apply a Charcoal (`#2B2D32`) overlay at 60–75% opacity. Text should be Stone (`#F4F3F0`).
- **Duotone (rare):** For abstract/editorial contexts, a duotone of Charcoal and Forest Green may be applied. Use sparingly — this is for blog headers or social media, not primary marketing.
- **Border radius:** Images on cards and in content use 12–16px border radius. Full-bleed hero images use no radius.

### 7.3 Aspect Ratios

| Context | Ratio | Notes |
|---|---|---|
| Hero banner | 16:9 or 2.4:1 | Full-width, above the fold |
| Blog/article header | 16:9 | Standard landscape |
| Card thumbnail | 4:3 | Content cards, case studies |
| Team photo | 1:1 | Circular crop, 50% border-radius |
| Social media | Platform-specific | See Applications section |

---

## 8. UI Components

### 8.1 Buttons

**Primary Button**
```
Background:     linear-gradient(135deg, #3D6B5E, #4D8272)
Text:           #FFFFFF, Karla SemiBold, 14.5px
Padding:        14px 28px
Border-radius:  12px
Shadow:         0 2px 12px rgba(61, 107, 94, 0.2)
Hover:          translateY(-1px), shadow increases to 0 4px 20px rgba(61, 107, 94, 0.27)
Active:         translateY(0), shadow decreases
```

**Secondary Button (Ghost)**
```
Background:     transparent
Border:         1.5px solid #D4D3D0
Text:           #6E7074, Karla Medium, 14.5px
Padding:        14px 24px
Border-radius:  12px
Hover:          border-color transitions to rgba(61, 107, 94, 0.33), text colour to #2B2D32
```

**Tertiary Button (Text)**
```
Background:     none
Text:           #3D6B5E, Karla Medium, 14px
Padding:        8px 0
Hover:          gap between text and arrow increases from 4px to 8px
```

**Button Rules:**
- Buttons always use Karla, never Libre Baskerville.
- Maximum one primary button per visible viewport. Two primary buttons competing for attention violates our restraint principle.
- Never use all-uppercase text on buttons.
- Icon + text buttons: icon goes on the right (trailing), 8px gap.
- Minimum touch target: 44×44px.

### 8.2 Cards

```
Background:     #FFFFFF
Border:         1px solid rgba(43, 45, 50, 0.07)
Border-radius:  16px
Padding:        36px
Shadow:         none (default), 0 4px 24px rgba(0,0,0,0.04) on hover
Hover:          border-color transitions to rgba(61, 107, 94, 0.25), translateY(-2px)
Transition:     all 0.3s ease
```

Card content order (top to bottom):
1. Icon or category label (optional)
2. Title (Libre Baskerville or Karla heading-md)
3. Body text (Karla body)
4. Link or CTA (optional, tertiary button style)

### 8.3 Input Fields

```
Background:     #FFFFFF
Border:         1.5px solid #D4D3D0
Border-radius:  10px
Padding:        12px 16px
Font:           Karla Regular, 15px, #2B2D32
Placeholder:    #6E7074
Focus:          border-color transitions to #3D6B5E, box-shadow: 0 0 0 3px rgba(61, 107, 94, 0.1)
Error:          border-color: #B04040, helper text in #B04040
```

- Labels sit above input fields, Karla Medium 13px, Charcoal.
- Helper text below input, Karla Regular 13px, Warm Grey.
- Required field indicator: a small Forest Green dot, not an asterisk.

### 8.4 Navigation

**Desktop Header:**
```
Height:         72px
Background:     transparent (scrolled: #F4F3F0 with subtle shadow)
Logo:           Left-aligned, full lockup
Nav items:      Karla Medium, 14px, Warm Grey, 36px gap between items
                Hover: Charcoal colour transition
CTA:            Secondary button style (ghost), right-aligned
```

**Active page indicator:** A 2px Forest Green underline, 4px below the text, animated in with a width transition.

**Mobile:** Hamburger menu. Full-screen overlay on Stone background. Navigation items in Libre Baskerville, 28px, vertically stacked with 24px gap.

### 8.5 Pills & Tags

```
Background:     rgba(61, 107, 94, 0.1)
Border:         1px solid rgba(61, 107, 94, 0.2)
Text:           #3D6B5E, Karla Medium, 12.5px
Padding:        6px 14px
Border-radius:  100px (full pill)
```

Optional leading dot: 6px circle, `#3D6B5E`, 8px gap to text.

### 8.6 Stat / Metric Displays

```
Value:          Libre Baskerville, 30–36px, Forest Green (#3D6B5E)
Label:          Karla Medium, 13px, Warm Grey (#6E7074)
Container:      Card style (white, rounded, bordered)
Arrangement:    Horizontal row of 3 on desktop, vertical stack on mobile
```

### 8.7 Hero CTA Banner (Dark)

```
Background:     linear-gradient(165deg, #2B2D32 0%, #3E4048 40%, #505460 100%)
Border-radius:  20px
Padding:        72px 64px
Text:           Stone (#F4F3F0)
Muted text:     rgba(244, 243, 240, 0.6)
Decoration:     Subtle vertical lines (see §6.4)
CTA:            Primary button (green gradient)
```

---

## 9. Motion & Animation

### 9.1 Principles

Motion in Meridian interfaces should feel **purposeful and restrained** — it clarifies changes, guides attention, and adds subtle polish. It should never feel playful, bouncy, or attention-seeking.

### 9.2 Timing

| Type | Duration | Easing | Usage |
|---|---|---|---|
| Micro (hover, focus) | 150–200ms | `ease` | Colour changes, shadows, borders |
| Standard (open/close) | 250–300ms | `ease-in-out` | Dropdowns, modals, accordions |
| Page transition | 300–400ms | `ease-out` | Page enters, section reveals |
| Emphasis | 400–600ms | `cubic-bezier(0.4, 0, 0.2, 1)` | Hero text entrance, stat counters |

### 9.3 Approved Animations

| Animation | Description | Context |
|---|---|---|
| **Fade + slide up** | Element fades in while translating up 12–20px | Page load reveals, scroll-triggered content |
| **Hover lift** | `translateY(-1px)` to `translateY(-2px)` + shadow increase | Buttons, cards |
| **Width expand** | Underline or divider grows from 0% to 100% width | Active nav indicator, section entrance |
| **Staggered reveal** | Sequential fade-in with 60–100ms delay between items | Card grids, service lists, stat rows |
| **Arrow nudge** | Arrow icon moves right by 4px on hover | Tertiary links (e.g., "All services →") |

### 9.4 Forbidden Animations

- Bounce or elastic easing
- Rotation or spin effects on UI elements
- Parallax scrolling on text
- Auto-playing carousels or slideshows
- Scale effects larger than 1.02x
- Any animation longer than 600ms
- Looping animations (except loading spinners)

---

## 10. Voice & Tone

### 10.1 Writing Principles

1. **Lead with clarity.** Every sentence should make the reader smarter. Remove any word that doesn't earn its place.
2. **Be specific over generic.** "We reduced documentation time by 92% for 400+ clinicians" > "We help healthcare organisations with AI."
3. **Use active voice.** "We deploy AI systems" > "AI systems are deployed by our team."
4. **Avoid jargon reflexively.** Use clinical or technical terms when they're the right word for the audience — but never to impress.
5. **Respect the reader's intelligence.** Don't over-explain. Don't hedge with excessive qualifiers.
6. **One idea per sentence when possible.** Short sentences convey confidence.

### 10.2 Tone Spectrum

| Context | Tone | Example |
|---|---|---|
| Website hero | Confident, direct | "AI that understands how clinicians work" |
| Case study | Precise, evidence-based | "Documentation time fell from 14 minutes to 90 seconds per encounter" |
| Blog post | Thoughtful, engaged | "Here's what we learned deploying NLP in a 200-bed hospital" |
| Email outreach | Warm, professional | "I'd love to understand what's slowing your team down" |
| Social media | Concise, credible | "6 years building healthcare AI. 400+ clinicians. One focus." |
| Error message | Calm, helpful | "We couldn't process that request. Here's what you can try." |

### 10.3 Vocabulary

| Use | Avoid |
|---|---|
| Clinician, physician, provider | User, customer, client (in clinical contexts) |
| Deploy, integrate, implement | Leverage, synergise, revolutionise |
| Clinical workflow | Patient journey (unless literally about the patient) |
| AI system, model | AI solution, AI-powered (overused) |
| We help... | We empower... (empty) |
| Reduced by X% | Dramatically improved (vague) |
| Built for | Designed for (unless literally about design) |

### 10.4 Formatting Conventions

- **Numbers:** Use figures for all numbers in marketing copy. "6 years" not "six years." Exception: beginning a sentence.
- **Percentages:** Use the `%` symbol. "92%" not "ninety-two percent."
- **Dates:** 6 February 2026 (day month year, no commas). Never use ordinal suffixes (6th).
- **Em dashes:** Use a spaced em dash ( — ) for parenthetical asides.
- **Oxford comma:** Always.
- **Ampersands:** Only in headings or space-constrained contexts. Never in body text.
- **Capitalisation:** Sentence case for headings. Title Case only for the company name and proper nouns.

---

## 11. Applications

### 11.1 Website

- **Framework:** Next.js (React) or equivalent static-first framework.
- **Background:** Stone (`#F4F3F0`). No pattern, no texture.
- **Max width:** 1200px, centred, 48px side padding on desktop.
- **Hero section:** Text-dominant. No hero images unless they are real (not stock). Generous whitespace above and below.
- **Footer:** Charcoal background, Stone text. Minimal — logo, nav links, contact, legal. No newsletter signup in the footer unless it earns its place.

### 11.2 Presentation Decks

- **Tool:** Keynote, Google Slides, or Figma.
- **Aspect ratio:** 16:9.
- **Title slide:** Charcoal background, Libre Baskerville heading in Stone, overline label in Forest Green.
- **Content slides:** Stone background, Charcoal text. One idea per slide.
- **Data slides:** Use Forest Green for the primary data series, Charcoal for secondary, Warm Grey for tertiary.
- **Typography:** Same system as web — Libre Baskerville for titles, Karla for body.
- **Slide numbers:** Bottom right, Karla 11px, Warm Grey.
- **No slide transitions.** Simple cut between slides.

### 11.3 Documents (Reports, Proposals, Contracts)

- **Paper:** A4 for European audiences, US Letter for American.
- **Margins:** 1 inch / 25mm all sides.
- **Title page:** Charcoal "MERIDIAN" wordmark, tracked widely. Document title in Libre Baskerville. Overline label in Forest Green. Date and confidentiality note in Warm Grey.
- **Body:** Karla Regular, 11pt, 1.5 line spacing. Justified alignment is acceptable in formal documents; left-aligned otherwise.
- **Headers:** Libre Baskerville, 14pt (H1), 12pt (H2). Karla SemiBold 11pt (H3).
- **Page numbers:** Bottom centre, Karla 9pt, Warm Grey.
- **Running header:** "Meridian Brand Guidelines" (or document title), right-aligned, Karla 8pt, Warm Grey.

### 11.4 Email Signatures

```
[Name]
[Title] · Meridian

[phone] · [email]
meridian.health
```

- Font: System default (the recipient's email client controls rendering).
- No images, no logos in signatures (they display inconsistently and add attachment weight).
- Keep to 4 lines maximum.

### 11.5 Social Media

| Platform | Image Size | Notes |
|---|---|---|
| LinkedIn | 1200×627px | Stone background, Charcoal text, Green accent |
| Twitter/X | 1600×900px | Same palette. Bold stat or single quote per card. |
| Instagram | 1080×1080px | Editorial style. Libre Baskerville headline on Stone. |

- Social cards use the brand palette on Stone backgrounds. No photography on social unless it's genuinely strong.
- One idea per card. If you need to say more, use a carousel.
- Always end LinkedIn posts with a single clear CTA, not a list of hashtags.

---

## 12. Accessibility

### 12.1 Colour Contrast

All text must meet **WCAG 2.1 AA** standards as a minimum. Key contrast ratios in our palette:

| Combination | Ratio | Pass? |
|---|---|---|
| Charcoal on Stone | 10.2:1 | ✓ AAA |
| Charcoal on White | 12.6:1 | ✓ AAA |
| Forest Green on White | 4.9:1 | ✓ AA |
| Forest Green on Stone | 4.5:1 | ✓ AA (borderline — use ≥16px text) |
| Warm Grey on White | 4.6:1 | ✓ AA |
| Warm Grey on Stone | 3.8:1 | ✗ Use only for ≥18px or non-essential text |
| Stone on Charcoal | 10.2:1 | ✓ AAA |

### 12.2 Rules

1. **Never rely on colour alone** to communicate meaning. Always pair colour with text, icons, or patterns.
2. **Focus states** must be visible — use a 3px Forest Green outline with 2px offset on all interactive elements.
3. **Minimum text size:** 13px for any visible text. 16px minimum for primary content.
4. **Touch targets:** Minimum 44×44px for all interactive elements.
5. **Alt text:** Every image must have descriptive alt text. Decorative images use `alt=""`.
6. **Heading hierarchy:** Never skip heading levels (e.g., H1 → H3 without H2).
7. **Reduced motion:** Respect `prefers-reduced-motion`. All animations should have a static fallback.
8. **Screen reader testing:** Test all key flows with VoiceOver (macOS/iOS) and NVDA (Windows) before launch.

---

## 13. Don'ts & Common Mistakes

### Visual Identity

| ✗ Don't | ✓ Do Instead |
|---|---|
| Use light blue, teal, or any colour outside the palette | Stick to the approved Colour System |
| Use stock photography of stethoscopes or generic lab coats | Commission real photography or use text-only layouts |
| Use rounded, playful sans-serif fonts (e.g., Nunito, Poppins) | Use Karla for body, Libre Baskerville for display |
| Apply Forest Green as a large background fill | Use Charcoal for dark sections; Green is an accent only |
| Use gradients on text | Use solid Forest Green or Charcoal on text |
| Add decorative shapes, blobs, or abstract illustrations | Let whitespace and typography do the work |
| Use more than one primary CTA button per viewport | Choose one primary action; demote others to secondary |
| Mix serif and sans-serif inconsistently | Serifs are for headings and display; sans-serif for body and UI |

### Typography

| ✗ Don't | ✓ Do Instead |
|---|---|
| Set body text wider than 680px | Constrain body text columns to 65–75 characters |
| Use Bold (700) in body text | Use SemiBold (600) for emphasis |
| Use italic Libre Baskerville for headings | Italic Baskerville is only for pull quotes |
| Use Title Case in headings | Use sentence case: "From strategy to production" |
| Center-align body paragraphs | Left-align all body text; centre only hero headlines if needed |

### Tone & Content

| ✗ Don't | ✓ Do Instead |
|---|---|
| Say "leverage", "synergise", "revolutionise", "empower" | Use precise, active verbs: build, deploy, reduce, integrate |
| Make claims without evidence | Quantify everything: numbers, percentages, timeframes |
| Use exclamation marks in marketing copy | Let the content carry the energy. Period. |
| Write paragraphs longer than 4 sentences | Break up dense content. One idea per paragraph. |
| Open with "Welcome to..." or "We are pleased to..." | Open with a claim, insight, or the reader's problem |

---

## Appendix A: CSS Custom Properties

```css
:root {
  /* Colours */
  --color-charcoal: #2B2D32;
  --color-charcoal-light: #3E4048;
  --color-green: #3D6B5E;
  --color-green-light: #4D8272;
  --color-green-pale: #E8F0ED;
  --color-stone: #F4F3F0;
  --color-stone-dark: #EAEAE6;
  --color-white: #FFFFFF;
  --color-muted: #6E7074;
  --color-border: #D4D3D0;
  --color-border-light: #E8E7E4;
  --color-error: #B04040;
  --color-warning: #B08A40;

  /* Gradients */
  --gradient-accent: linear-gradient(135deg, #3D6B5E, #4D8272);
  --gradient-hero: linear-gradient(165deg, #2B2D32 0%, #3E4048 40%, #505460 100%);

  /* Typography */
  --font-display: 'Libre Baskerville', Georgia, 'Times New Roman', serif;
  --font-body: 'Karla', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-mono: 'IBM Plex Mono', 'Courier New', monospace;

  /* Spacing */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;

  /* Border Radius */
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-xl: 20px;
  --radius-full: 100px;

  /* Shadows */
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.04);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.08);
  --shadow-accent: 0 2px 12px rgba(61, 107, 94, 0.2);

  /* Transitions */
  --transition-fast: 150ms ease;
  --transition-base: 250ms ease-in-out;
  --transition-slow: 400ms cubic-bezier(0.4, 0, 0.2, 1);
}
```

## Appendix B: Figma Token Structure

If building a Figma design system, mirror the CSS custom properties above as Figma variables:

```
Primitives/
  Colour/Charcoal, Charcoal Light, Green, Green Light, ...
  Space/1, 2, 3, 4, 6, 8, 10, 12, 16, 20, 24
  Radius/sm, md, lg, xl, full
  
Semantic/
  Colour/Text Primary, Text Secondary, Text Muted, ...
  Colour/Background Page, Background Surface, Background Elevated
  Colour/Border Default, Border Light, Border Accent
  Colour/Interactive Default, Interactive Hover, Interactive Active

Components/
  Button/Primary, Secondary, Tertiary
  Card/Default, Hover
  Input/Default, Focus, Error
  Navigation/Default, Active
```

## Appendix C: File Naming Conventions

```
meridian-logo-full-dark.svg         Logo lockup on dark backgrounds
meridian-logo-full-light.svg        Logo lockup on light backgrounds
meridian-mark-gradient.svg          Square mark only
meridian-wordmark-charcoal.svg      Wordmark only, Charcoal
meridian-wordmark-stone.svg         Wordmark only, Stone (for dark bg)
meridian-og-linkedin.png            Social card template, LinkedIn
meridian-og-twitter.png             Social card template, Twitter/X
```

---

*This document is the single source of truth for all Meridian visual and verbal design decisions. If something isn't specified here, default to the principles in §1.5: restraint, material honesty, earned attention, quiet confidence. When in doubt, remove rather than add.*

**Last updated:** February 2026
**Owner:** Brand & Design
**Review cadence:** Quarterly

