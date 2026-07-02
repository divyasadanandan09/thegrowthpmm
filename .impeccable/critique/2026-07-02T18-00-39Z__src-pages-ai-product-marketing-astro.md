---
target: /ai-product-marketing
total_score: 29
p0_count: 0
p1_count: 1
timestamp: 2026-07-02T18-00-39Z
slug: src-pages-ai-product-marketing-astro
---
## Design Health Score — /ai-product-marketing

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | Marketing page; n/a mostly |
| 2 | Match System / Real World | 4 | Sharp, plain-spoken, anti-hype voice |
| 3 | User Control & Freedom | 3 | Back-to-home + CTA; no persistent nav |
| 4 | Consistency & Standards | 2 | Drifted from the homepage: CTA "Book a call" (home now "Book free consultation"), uppercase .eyebrow vs home's handwritten kickers, emoji icons vs home's monoline SVG |
| 5 | Error Prevention | 3 | n/a |
| 6 | Recognition vs Recall | 3 | Clear headers + accordion |
| 7 | Flexibility & Efficiency | 3 | Single path |
| 8 | Aesthetic & Minimalist | 2 | Uppercase tracked .eyebrow on every section (4x) + emoji icons = AI tells |
| 9 | Error Recovery | 3 | n/a |
| 10 | Help & Documentation | 3 | The page is explanatory content |
| **Total** | | **29/40** | **Good (lower end)** |

## Anti-Patterns Verdict
Detector: 0 findings (the eyebrow/emoji tells aren't in its ruleset). LLM: the writing is genuinely strong (POV, honest, specific), but the page kept the OLD system the homepage has since moved past — `.eyebrow` uppercase-tracked kickers above every section (the named "tiny uppercase eyebrow on every section" tell, x4: "The honest version / In practice / Where it breaks / Straight answers"), emoji workflow icons, and the "Book a call" CTA label.

## Priority Issues
- **[P1] Uppercase `.eyebrow` on every section (x4).** The homepage retired this for thinned handwritten Caveat kickers; this page still stacks an uppercase tracked label above each H2. It's the clearest AI-scaffold tell and the biggest cross-page inconsistency. Fix: switch to the handwritten-kicker cadence (and thin it), or drop the eyebrows. /impeccable typeset
- **[P2] Emoji workflow icons.** The four workflow cards use emoji chips; the homepage just replaced its emoji with a monoline SVG set. Fix: same monoline treatment for consistency. /impeccable colorize
- **[P2] CTA label "Book a call."** Homepage standardized to "Book free consultation" this session. Fix: unify. /impeccable clarify
- **[P3] Four identical channel-cards** (icon+heading+text). Mild identical-grid; acceptable but could vary hierarchy.

## Minor
- No persistent nav (only Back-to-home + one CTA) — fine for a pillar page.
- Closing reassurance "A 20-minute call, no pitch" is close to the home wording but not identical.
