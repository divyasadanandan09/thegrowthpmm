# The Growth PMM — design conventions

Brand for **Divya Sadanandan / TheGrowthPMM**, an independent product marketing consultant. Palette: **lime + near-black + coral**. Read this before styling anything for this brand.

## Setup
Import `styles.css` first — it pulls in fonts and tokens via `@import`, then the class vocabulary below. No provider/wrapper component is required; everything is CSS custom properties + utility classes on plain markup.

```html
<link rel="stylesheet" href="styles.css">
```

## The hard rule: lime is fill-only
`--navy` is the brand lime `#DBFF00` (name kept from before the 2026-07-01 rebrand — don't be misled by it). Lime is used **only** as:
- a **fill** (buttons, badge chips, the featured-card border) with **dark `--ink` text on top**, or
- an **accent on the near-black `--ink-deep` surfaces** (handwritten cursive, highlights).

**Never** lime text on a light background — contrast is ~1.1:1, unreadable. Dark sections (footer, closing bands, the "yes, if" compare card) use `--ink-deep` (#16180f), not lime, as their fill.

## Tokens (`tokens/tokens.css`)
| Token | Value | Use |
|---|---|---|
| `--navy` | `#DBFF00` | brand lime — fills only |
| `--navy-press` | `#c4e600` | lime hover/press |
| `--ink` | `#1d1d1d` | primary text |
| `--ink-mute` | `#5f6470` | secondary text |
| `--ink-deep` | `#16180f` | near-black surface |
| `--canvas` | `#ffffff` | page background |
| `--cream` | `#e7ebf5` | tinted section bg |
| `--blue-tint` | `#eef2fc` | pale tint fill |
| `--hairline` / `--warm-line` | `#e6e6e6` / `#d6dcec` | borders |
| `--link` | `#2f5fe0` | hyperlinks (the one blue; not a brand color) |
| `--coral` | `#cc4117` | supporting accent, means "drop-off" — use sparingly, only where something represents loss/friction |
| `--font-display` | Bricolage Grotesque | all headings (h1–h3) |
| `--font-body` | Inter | body copy, UI |
| `--font-hand` | Caveat | playful kickers only, never body copy |

## Class vocabulary (`styles.css`)
- **Buttons**: `.btn-navy` (primary CTA, lime fill/dark text), `.btn-outline-navy` (white + lime border), `.btn-tint` (pale fill). All pill-shaped (`border-radius: 90px`).
- **`.sticky-tag.purple`** = lime fill + dark text; **`.sticky-tag.gold`** = near-black fill + lime text. Both rotate slightly (rubber-stamp note look). Names are historical, ignore the color words.
- **`.marker`** = inline lime highlighter for emphasis in headings/body, light backgrounds only.
- **`.handwritten`** = Caveat, dark ink, for short kickers above a heading. **`.handwritten.light`** = same but lime, only on dark surfaces.
- **`.module` / `.module--featured`** = white bordered service cards; the featured variant gets a lime border + stronger shadow.
- **`.compare-card` / `.compare-card--me`** = light "alternative" card with red ✗ marks vs. the dark `--ink-deep` "the answer" card with green ✓ marks.
- **`.eyebrow`** = small uppercase utility label (12px, letterspaced) — legacy/utility contexts, not the primary kicker style (that's `.handwritten`).

## Voice, if generating copy alongside layout
Second person to the reader ("you/your"), first person when Divya speaks about herself. Zero em dashes. `$` for money, not other currency symbols. Icons are monoline SVGs (viewBox 24×24, stroke-width 1.8) — never emoji as UI icons.

## Where the truth lives
- `tokens/tokens.css` — all custom properties, commented with intent.
- `styles.css` — the class vocabulary above, real definitions.
- `fonts/fonts.css` — the Google Fonts `@import`.
- Component previews under `components/` for worked examples of each pattern above.

---

## About this sync

This project was built by a **hand-authored, off-script sync** from the [thegrowthpmm](https://www.thegrowthpmm.com) Astro codebase — not the standard `/design-sync` component-bundle converter. That converter targets compiled, reusable JS/React components; this repo is a static Astro marketing site with inline page markup and exactly one small reusable component (a logo mark), so there was no component library to import. What's here instead is the site's real design language: tokens, fonts, and class vocabulary, verified to actually match the live build.

## What's included

| Path | Contents |
|---|---|
| `tokens/tokens.css` | Every custom property from the site's `:root` block — palette, type, surfaces, the hero gradient. |
| `fonts/fonts.css` | The real Google Fonts `@import` (Bricolage Grotesque, Inter, Caveat) used in production. |
| `styles.css` | Entry point. Imports fonts + tokens, then the reusable class vocabulary (buttons, sticky tags, marker, handwritten, module cards, compare cards). |
| `components/foundations/Palette` | Visual swatch reference for every color token. |
| `components/foundations/Typography` | Live specimens of the three type faces and their roles. |
| `components/components/Buttons` | `.btn-navy` / `.btn-outline-navy` / `.btn-tint`, on light and dark. |
| `components/components/StickyTags` | `.sticky-tag.purple` / `.gold`, `.marker`, `.handwritten` / `.light`. |
| `components/components/CompareCards` | The "good fit / not a fit" comparison card pattern. |
| `components/brand/Logo` | The lime badge + funnel mark, navy and reverse variants. |

## Not included (out of scope for this sync)
- No `_ds_bundle.js` — there is no compiled component library to expose at runtime.
- No page templates (hero, services grid, etc.) — those are page-specific Astro markup, not reusable components, and reproducing them here would misrepresent them as a component API.
- No `_ds_sync.json` anchor — a future re-sync of this repo re-verifies everything rather than diffing against a component build; that's correct for a hand-authored layout with no compiled source to hash.

## Verification
Every preview card in `components/` was rendered in a browser and visually checked against the live site's actual rendering of the same pattern (colors, type, spacing, rotation) before upload. Every class and token named in the conventions above was grep-verified to exist in the shipped `styles.css` / `tokens/tokens.css`.
