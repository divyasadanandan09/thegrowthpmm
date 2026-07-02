---
target: the homepage (post-overhaul)
total_score: 31
p0_count: 0
p1_count: 2
timestamp: 2026-07-02T10-16-47Z
slug: src-pages-index-astro
---
## Design Health Score

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | Nav collapses to a corner CTA on scroll; no on-page booking feedback (booking is external, acceptable) |
| 2 | Match System / Real World | 4 | Founder's language throughout; "PMM" acronym in hero body is the one unglossed term |
| 3 | User Control and Freedom | 3 | Clear nav + mobile menu; external booking opens new tab |
| 4 | Consistency and Standards | 3 | CTA now unified ("Book free consultation"); but eyebrow cadence + icon language (emoji vs. the custom diagram) drift |
| 5 | Error Prevention | 3 | No on-page forms; n/a mostly |
| 6 | Recognition Rather Than Recall | 4 | Visible nav, labelled links, clear section headers |
| 7 | Flexibility and Efficiency | 3 | One primary path (call) + soft path (audit); fine for a marketing page |
| 8 | Aesthetic and Minimalist Design | 2 | Slop creep in the new middle sections: a side-stripe border (hard ban), 4 identical service cards, 3 identical mini-cards, text-heavy hero |
| 9 | Error Recovery | 3 | n/a for marketing |
| 10 | Help and Documentation | 3 | FAQ + AI PMM pillar pages, reassurance copy |
| **Total** | | **31/40** | **Good** |

## Anti-Patterns Verdict

**LLM assessment:** The site's *identity* is genuinely distinctive — lime + near-black + Bricolage Grotesque with Caveat scrapbook accents, and a custom hub-and-spoke positioning diagram that teaches instead of decorating. That passes the "which AI made this?" bar in the hero. But the 2026-07-02 overhaul introduced slop creep in the middle of the page: the Services section is now **four identical icon+heading+text cards** (a named ban), Section 2 stacks **three identical cream label-cards** plus a **side-stripe border** on the punchline, and the hero is now text-heavy. The top and identity are strong; the middle regressed toward template-land.

**Deterministic scan:** `detect.mjs` returned **1 finding (warning): `side-tab` at index.astro:157** — `border-left:3px solid var(--navy)` on the Section 2 "Yet nobody owns the story…" callout. This is a true positive and a hard ban in the skill. The LLM review independently flagged the same element plus card-sameness the detector doesn't check.

## Overall Impression

The repositioning to "the first Product Marketing leader you hire before you're ready to hire one" is a real strategic upgrade — it names the role and the moment, which the old "unlock your next growth stage" never did. The hero H1, the diagram, and the Before/After table carry that story well. The single biggest opportunity: the two new narrative sections and the Services grid reintroduced the exact card-and-accent tells the rest of the site worked hard to avoid. Fix those three and the page reads as premium end-to-end.

## What's Working

- **The positioning diagram.** A custom SVG that *teaches* (Product/Sales/Marketing → The Growth PMM), not a stock illustration. On-brand, distinctive, and it now reinforces the exact H1 claim. Genuine craft.
- **The Before/After table (Section 3).** A clean, non-carded 2-column comparison with hairline rows and a "→" glyph. This is the right way to show transformation — restrained and premium.
- **Positioning clarity.** "The Product Marketing leader you need, before you're ready to hire one" + the honest "Are we a good fit? / Probably not, if…" block is confident and self-qualifying — exactly the senior, plain-spoken voice the brand wants.

## Priority Issues

- **[P1] Side-stripe border on the Section 2 punchline** (index.astro:157). A 3px lime `border-left` on the "Yet nobody owns the story that connects them." callout. This is the single most recognizable AI-UI tell and a hard ban; the detector caught it.
  - **Why it matters:** it undercuts the "practice what you preach / sharp craft" principle on the very line meant to land the argument.
  - **Fix:** drop the border-left. Make it a full-width statement instead — larger Bricolage weight, a lime `.marker` highlight on "nobody owns the story," or a quiet full hairline above/below. No colored side bar.
  - **Suggested command:** /impeccable layout

- **[P1] Services is four identical cards.** Icon-chip + heading + paragraph, ×4 in a 2×2 grid — the "identical card grid" ban, plus emoji-in-rounded-chip icons that read templatey for a senior offer.
  - **Why it matters:** the old Services was deliberately varied (a featured module + secondary pair). This flattened it into the most generic SaaS pattern, right where you describe the actual work.
  - **Fix:** break the sameness — feature the first outcome larger, alternate a 2-col editorial list, or drop the cards for numbered outcomes with real hierarchy. At minimum, retire the emoji chips for a restrained monoline mark or a numbered treatment.
  - **Suggested command:** /impeccable layout

- **[P2] Section 2's three "Product / Marketing / Sales" cards.** Three identical cream cards with tiny uppercase tracked labels — two tells stacked (identical grid + eyebrow-style labels). Ironically they're meant to show *disconnected* pieces.
  - **Why it matters:** it's decorative packaging around six words; the point ("nobody connects them") would land harder shown as genuinely separate, unjoined fragments than as three matching boxes.
  - **Fix:** make it one editorial line, or three fragments with visible gaps/misalignment (show the disconnect), not three tidy cards. Drop the uppercase labels.
  - **Suggested command:** /impeccable distill

- **[P2] Text-heavy hero.** H1 (2 lines) + bold sub-line (2 lines) + 5-line body paragraph + reassurance line + CTA. That's a lot of reading at the peak-impression moment.
  - **Why it matters:** the diagram already carries the "connective function" idea; the stacked copy competes with it and pushes the CTA down.
  - **Fix:** cut or shorten the body paragraph (the sub-line + diagram already say it), or merge the sub-line into the body. Let the H1 + one supporting line + CTA breathe.
  - **Suggested command:** /impeccable distill

- **[P3] Emoji icons across Services + Recognition band** (🎯🚀💬⚙️ / 🏆💰⭐). Emoji read informal and render inconsistently across platforms — a slightly casual note in an otherwise premium, senior offer.
  - **Fix:** swap for a restrained monoline SVG set, or lean on numerals/typography.
  - **Suggested command:** /impeccable typeset

## Persona Red Flags

**Skeptical post-PMF founder (project persona):** Lands on a text-heavy hero and has to read four stacked blocks before the CTA. Wants proof fast — the real named numbers ($11M+, 7.35x) sit far down past two narrative sections and a 4-card grid. The identical service cards + emoji risk reading as "templated consultant," the exact impression the honesty angle is meant to defeat.

**Jordan (first-timer):** The diagram teaches the core idea well within 5 seconds. One snag: the hero body says "without the cost of a full-time PMM executive" — "PMM" isn't expanded until later. Mild jargon barrier at first contact.

**Casey (mobile):** CTA docks to the thumb zone (good). But the page is now a long stack of cards on mobile — 3 ownership cards + 4 service cards + the table rows — so the middle is a lot of vertical scrolling through similar-looking boxes.

## Minor Observations

- Terminology drift: primary CTA says "Book free consultation" while the hero reassurance still says "A 20-minute call." Align to one word (consultation/call).
- `Layout.astro` `<title>`/meta/schema still describe the old "Fractional Head of Product Marketing" framing — now out of sync with the "first PMM leader" positioning (SEO/AEO mismatch).
- The "Only 3 clients per month" tag now sits above a longer 2-line H1; confirm it doesn't feel cramped at desktop.
- Dead CSS from the retired Services structure (`.module--featured`, `.channel-grid`, `.channel-card`) is now unused.

## Questions to Consider

- Section 2 and Section 3 both make the same argument (founders can't own the connecting story / here's the before→after). Does the page need both, or would one sharper section hit harder?
- The hero now carries the whole positioning in copy AND in the diagram. If you trust the diagram, how much of the body paragraph can you cut?
- What would the Services section look like with zero cards — could the four outcomes be a numbered, typographic list that matches the editorial Before/After table right above it?
