---
target: the site (after de-slop + Section 3 polish)
total_score: 34
p0_count: 0
p1_count: 0
timestamp: 2026-07-02T10-38-26Z
slug: src-pages-index-astro
---
## Design Health Score

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | Nav collapses to a corner CTA on scroll; booking is external (fine) |
| 2 | Match System / Real World | 4 | Founder's language; hero "PMM executive" jargon removed this pass |
| 3 | User Control & Freedom | 3 | Clear nav + mobile menu; booking opens a new tab |
| 4 | Consistency & Standards | 4 | CTA unified ("Book free consultation"); icons now one monoline family; meta realigned |
| 5 | Error Prevention | 3 | No on-page forms; mostly n/a |
| 6 | Recognition vs Recall | 4 | Visible nav, labelled links, clear headers |
| 7 | Flexibility & Efficiency | 3 | One primary path + soft audit path; right for marketing |
| 8 | Aesthetic & Minimalist | 4 | Slop tells gone; distinctive identity end-to-end. Minor: page length + a couple of conventional label patterns |
| 9 | Error Recovery | 3 | n/a for marketing |
| 10 | Help & Documentation | 3 | FAQ + AI PMM pillar, reassurance copy |
| **Total** | | **34/40** | **Good (upper end)** |

## Anti-Patterns Verdict

**LLM assessment:** The middle-of-page slop the last critique flagged is gone. Services is now a featured "growth engine" block + three secondary cards (varied hierarchy, not an identical grid); Section 2's three cards became staggered unaligned fragments; the Section 2 side-stripe border is removed; every emoji is now a restrained monoline SVG in one consistent family. The identity (lime + near-black + Bricolage + Caveat, the custom hub diagram) now runs coherently from hero to close. Nobody would confidently say "an AI made this."

**Deterministic scan:** `detect.mjs` → **0 findings.** The side-tab warning from the prior run is cleared. No new tells introduced by the Section 3 polish (the 1px column hairline is allowed, not a side-stripe accent).

## Overall Impression

This is now a genuinely premium, distinctive page that reads as a senior, plain-spoken PMM leader. The repositioning + the de-slop pass moved it from "good with template creep in the middle" to "coherent end-to-end." The remaining opportunities are editorial (is the page saying the same thing twice?) and length, not craft. The single biggest lever left is deciding whether Section 2 and Section 3 both need to exist.

## What's Working

- **Section 3 (Before/After).** The struck-through, muted Before column against the pale-lime, bold After column carries the transformation with zero arrows. It's the strongest "here's what changes" device on the page and unmistakable at a glance.
- **De-slopped middle.** Services' featured-plus-secondary hierarchy and Section 2's staggered fragments both replaced identical-card patterns with something that actually means something. The monoline icon set reads senior, not casual.
- **Positioning + honesty.** "The Product Marketing leader you need, before you're ready to hire one," plus the "Yes, if / Probably not, if" block, is confident and self-qualifying. It sells by disqualifying, which is exactly the brand's edge.

## Priority Issues

- **[P2] Section 2 and Section 3 argue the same point back to back.** "Founders can't own the connecting story as you scale" (Section 2) and "before → after once PMM has an owner" (Section 3) are two runs at one idea, right next to each other, on a page that's already long.
  - **Why it matters:** momentum. A skeptical founder reads two conceptual sections before reaching proof; repetition reads as padding, the opposite of the sharp-positioning promise.
  - **Fix:** either merge them into one beat (keep the Before/After table, fold the complexity narrative into its intro), or sharpen Section 2 to a single line + the fragments and let Section 3 do the heavy lifting.
  - **Suggested command:** /impeccable distill

- **[P2] Proof sits deep on a long page.** On mobile especially, the reader passes hero → complexity → before/after → 4 service blocks → process before hitting the real numbers ($11M+, 7.35x).
  - **Why it matters:** the skeptical-founder persona wants evidence fast; the proof is the strongest trust asset and it's buried.
  - **Fix:** consider moving Proof (or a one-line proof teaser) above the two narrative sections, or trimming the pre-proof stack.
  - **Suggested command:** /impeccable layout

- **[P3] Decorative SVG icons lack `aria-hidden`.** The new Services and Recognition-band icons are purely decorative but aren't hidden from assistive tech.
  - **Fix:** add `aria-hidden="true"` (and `focusable="false"`) to each decorative `<svg>`.
  - **Suggested command:** /impeccable audit

- **[P3] Proof stat labels are tiny uppercase tracked text** ("GROWTH & EXPERIMENTATION", "PAID ACQUISITION TURNAROUND", ×4). Borderline eyebrow-tell, though conventional as data labels above numbers.
  - **Fix:** optional; sentence-case or drop to plain small-caps if you want to shed the last uppercase-tracked pattern.
  - **Suggested command:** /impeccable typeset

## Persona Red Flags

**Skeptical post-PMF founder:** Hero is tighter now (good), but proof is still deep behind two conceptual sections. Wants the numbers sooner.

**Jordan (first-timer):** Hero jargon reduced ("full-time hire" not "PMM executive"). "PMM" still appears in the Before/After table and the brand mark, but context now carries it. No real barrier left.

**Casey (mobile):** CTA is thumb-docked (good). The page is still a long vertical stack; the two adjacent narrative sections add to the scroll before proof.

## Minor Observations

- Hero `.marker` on "before you're ready to hire one" wraps to two highlight boxes across the line break. On-brand (matches the H1 marker pattern) but slightly busy; fine to leave.
- Four handwritten Caveat eyebrows remain (Services, About, right-fit, Growth Audit). This is the deliberate brand system, not the uppercase-tracked tell, so it's defensible; just keep an eye on the cadence if you add more sections.
- Dead CSS from the retired Services structure (`.module--featured` is reused; `.channel-*` is still used on the AI page) — nothing to remove after all.

## Questions to Consider

- Do Section 2 and Section 3 both need to exist, or is the Before/After table alone sharper?
- Should proof come before the narrative, so the skeptical founder gets evidence before argument?
- Is "A repeatable growth engine" the right thing to feature in Services, given positioning is usually the foundational deliverable?
