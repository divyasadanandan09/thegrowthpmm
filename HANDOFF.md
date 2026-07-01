# Handoff — TheGrowthPMM site

Snapshot of where the site stands and why, so a fresh session can continue cleanly.
(High-level project context is in `CLAUDE.md`; this file is the detailed decision log + open items.)

## Conversion model: CALL-LED (changed 2026-06-24)

The site is now **call-led**, not lead-magnet-led. Every primary CTA is **"Book a call"** (label standardized site-wide). The free Growth Report is a **secondary, soft option**, demoted to a "not ready for a call yet?" section placed late on the page (after About, before the closing band).

Why: Divya takes only **four clients a month**. Low-volume, high-trust business, so a few good-fit calls beat a big email list. Leading with the report optimized for volume she doesn't want.

This **reverses** the earlier lead-magnet-led decision (report as the primary CTA everywhere). If older notes here or in `CLAUDE.md` still say lead-magnet-led, they're stale.

## Update 2026-06-25 — LLM-council review pass

Ran the site through an LLM council (Claude + GPT-5.2 + Gemini 3) on positioning, page flow, AEO/GEO, and conversion. Shipped this session:

**Hero is now symptom-led.** H1: "You found product-market fit. Then growth stalled. I find why, and fix it." Subtext names the failure modes (positioning, a channel, activation, pricing, sales motion) and the fractional-Head-of-PMM offer. Dropped "extended PMM team" and the orphan "Product marketing, as a service." closer. Category label is now **"Fractional Head of PMM"** (the searched term), not "PMM as a service."

**The "leak" metaphor was retired site-wide.** 16 copy spots across `index.astro`, `faq.astro`, and the Layout meta moved to **"drop-off / where growth stalls / the constraint."** The funnel visual stays; its caption is now "watch where it drops off." The Problem section eyebrow is "The stall," H2 "Finding the constraint is the hard part. Fixing it comes after." Don't reintroduce "leak."

**New homepage sections.**
- **How it works** (between Services and Proof): three steps, Find the constraint / Ship the fix / Embed and scale, plus a "What I need from you" line and an inline CTA. `.process-*` styles.
- **Testimonials** (after Proof): card 1 is an anonymized/representative quote (confirm or replace with a real anonymized client); cards 2 and 3 are **Samarth** and **Priyadarshi** (real LinkedIn recommendations) and still need their text + titles pasted in. LinkedIn blocks automated fetch, so Divya supplies the wording. `.testimonial-*` styles.
- **Inline CTAs** after How-it-works and Testimonials. This reverses the earlier "no mid-page inline CTA" rule.
- **Services restructured (2026-06-25):** modular, not a 1-2-3 sequence. Growth strategy is the featured/hero service; Positioning audit and Go-to-market are secondary "other services." See current-state item 5.

**Proof.** The middle stat card now leads with **"Master of Margin"** (the award) instead of "$60K"; the $60K moved into the detail so it stops reading small next to $11M+.

**Other copy.** Services intro ("on a fractional basis"); growth-strategy intro dropped ", not bets"; channel/GTM labels switched "&" → "and"; proof intro "Every number here is from real work"; FAQ cost answer now anchors "around $500 and scope from there."

**AEO / GEO.**
- **JSON-LD**: global `Person` + `ProfessionalService` graph in `Layout.astro` (every page); `FAQPage` on `/faq` and `/ai-product-marketing`.
- **Title/meta** rewritten to the searched term: "Fractional Product Marketing Consultant for B2B SaaS | TheGrowthPMM", meta carries an India/US geo signal.
- New **`/ai-product-marketing` pillar page** (answer-first: AI PMM POV, the workflows, guardrails, proof, a 4-Q FAQ). Linked from footer + mobile menu.

**The AI-PMM debate (resolved).** Council verdict: keep AI **out of the homepage core positioning**. Lead with the founder's outcome; build the "leading voice of AI PMM" identity on the pillar page + a content cluster, and surface AI on the homepage only as a capability, not a category. Revisit elevating AI into the hero once there are 2-3 AI-specific case snapshots.

**Booking qualification = native Google Calendar questions** (chosen over an on-site form or new SaaS). Can't be set from code. Divya adds these in Google Calendar → the appointment schedule → Booking form, as required questions:
1. What stage are you? (pre-PMF / post-PMF with first revenue / scaling)
2. What's your primary growth bottleneck right now? (short answer)
3. Monthly revenue or marketing budget band? (ranges of your choice)
Optional: "What have you already tried?" Keep the calendar link itself as the CTA target, no interstitial page.

## Update 2026-06-26 — copy revision pass (from Divya's edited COPY.md)

Applied a full copy revision across all three pages + `Layout.astro`. Highlights:

- **Brand display name → "The Growth PMM"** (with spaces) in nav, footer logo, home `<title>`, and the comparison card. Copyright, the `/faq` + `/ai-product-marketing` `<title>`s, and the JSON-LD schema still say one-word "TheGrowthPMM".
- **Hero rewritten** (symptom-led): H1 "You have paying users, but growth stalled? I'll find what's capping it, and fix it." Body now ends "full-time seniority, a fraction of the cost" (dropped the 2-week and lock-in lines). Funnel caption "Where are you losing users?"
- **"Free report" → "Growth Audit"** everywhere visible: nav link, section H2, CTAs ("Get FREE growth audit"), FAQ Q6 + closing. The `id="report"` and the `DIAGNOSTIC` Google Form var are unchanged.
- **"What I need from you" line removed** from How it works. Step 3 retitled "Scale the growth," copy trimmed.
- **Comparison**: "A full-time Head of PMM" vs "The Growth PMM", now 5 rows each (added "Split across the whole org…" and "Flat monthly fee"; "start in days, not months").
- **Proof**: dropped TCS from the proof intro line (still in the bio); added client contexts (Series E healthtech, traveltech, Practo, Fi Money); stat 4 is "a new category" not "insurance vertical"; stat 1 adds "lending".
- **FAQ**: several answers shortened; the "or book a strategy call" secondary link removed from the closing band (now audit-only; the top-bar "Book a call" remains).
- **AI page**: closing H2 "Want a Senior PMM who already works this way?"
- **Title/meta**: home title now "Product Marketing Consultant for B2B SaaS | The Growth PMM"; meta dropped "Senior".
- Fixed two typos from the source copy: "channel mix in healthy" → "stays healthy"; footer "Frctional" → "Fractional".

### Two contradictions — RESOLVED 2026-06-29
1. **Clients per month:** unified to **three** (the compare card "four" was changed to match the bio).
2. **Brand spelling:** unified to **"The Growth PMM"** everywhere visible (footer copyright, `/faq` + `/ai-product-marketing` titles, nav logos). The JSON-LD `ProfessionalService` now uses `name: "The Growth PMM"` with `alternateName: "TheGrowthPMM"` so the one-word form still resolves.

## Update 2026-06-29 — impeccable audit + critique pass
Ran `/impeccable audit` (14/20) and `/impeccable critique` (31/40). Shipped this session:
- **Palette de-warmed (was the cream/beige AI default).** `--cream` #f4ede4 → cool navy-tinted **#e7ebf5**; hero-bg aurora re-tinted to purple→navy→teal (echoes the funnel) instead of warm peach; warm border #e4d8c6 → `--warm-line` #d6dcec. Contrast re-verified (ink-mute ≥4.97:1). Warm icon-chip tints (#fdeee9/#fdf3da) kept as small accents.
- **Card-grid monotony broken (#9).** Two sections de-carded:
  - *Testimonials*: the 3 identical cards are now an editorial block — a featured lead pull-quote (Varun) with an oversized Caveat quote mark, then the two LinkedIn recs borderless under a hairline (`.testimonial-lead` / `.testimonial-pair`).
  - *Proof*: the 3 separate bordered stat cards became one white panel divided by hairlines (`.proof-strip` / `.proof-stat`; vertical dividers on desktop, horizontal when stacked), matching the divided-panel language of the `.proof-bottom` block below it.
  - Left intentionally as-is: Services (featured module + 2-up, not an identical grid), How it works (a real numbered sequence), Compare (a 2-col comparison).
- **Reduced-motion:** the funnel SMIL now freezes via `matchMedia` + `svg.pauseAnimations()` when the user opts out.
- **A11y:** funnel SVG got `role="img"` + `<title>`; the "Past experience" label contrast fixed (#a89a86 → #726551, 4.89:1); logo + photo images got width/height + `loading="lazy"`.
- **Naming:** footer "The free report" → "Growth audit"; the two contradictions above resolved.
- **DIAGNOSTIC** is still a placeholder, now a valid-shaped dummy `https://forms.gle/REPLACE-ME` (no longer a broken bracket string). Replace before launch.

## Update 2026-06-30 — "right fit" block + funnel arrow
- **About section comparison replaced.** The "Senior PMM leader, without the full-time bet" heading + the full-time-hire-vs-Growth-PMM ✗/✓ comparison are gone. In their place: an **"Is this the right fit?"** block — navy "A fit if" card (green ✓, 4 items) + white "Not a fit if" card (red ✗, 3 items), reusing the compare-card styles. More honest, self-qualifying, filters bad-fit calls. Cut from the source draft: a "regulated industry" disqualifier (contradicted the Fi Money/healthtech proof), "Series A-C"/"VP" ICP drift, and hours/part-time-price framing.
- **Funnel arrow:** a directional arrow was briefly added then removed; the funnel caption is just "Where are you losing users?" with no arrow glyph.

### Polish pass (2026-06-29, `/impeccable polish`)
- **Keyboard focus:** authored `:focus-visible` rings globally (navy ring; white on dark footer/closing-band buttons) — was relying on the UA default.
- **Reduced motion:** added a global `@media (prefers-reduced-motion: reduce)` fallback (kills transitions/animations + the CTA hover lift); complements the funnel SMIL pause.
- **Touch targets:** footer links now ~28px tall (`padding-block`), meeting WCAG 2.5.8 AA.
- **Micro-interaction:** primary `.btn-navy` gets a 1px hover lift on an ease-out curve (fixed a `#navbar a` specificity clash that was clobbering the pill CTA's transition).
- **Typography:** `text-wrap: pretty` on body `p`; `text-wrap: balance` extended to `h3`.
- **Copy consistency:** "Growth Audit" capitalized as the proper-noun offer everywhere (nav, footer, body, CTAs, FAQ); all-caps "FREE" toned to "the free Growth Audit".
- **Deliberately deferred:** white card surfaces are still hard-coded `#fff` (~25 inline spots). That's a `/impeccable extract` refactor (introduce a `--surface` token), not a polish-pass change — left as a follow-up to avoid risky mass find/replace across text-color vs background uses.

The editable copy decks at `COPY.md` (project) and `~/Downloads/TheGrowthPMM-COPY.md` are now STALE relative to the applied copy. The `.astro` files are the source of truth.

## Update 2026-07-01 — LIME REBRAND + content refresh (client-directed)

Divya asked to change the primary brand colour to **lime `#DBFF00`** and to refresh the homepage copy. This is intentional — **do not "correct" it back to navy.** Older notes in this file and `CLAUDE.md` that say "navy #1b2a6b primary" are now stale.

**Token model (the important part).** Navy played five roles; lime can only do some of them, so the roles were split:
- `--navy` = **lime `#DBFF00`** (kept the name to avoid renaming ~100 refs; it's a misnomer now). `--navy-press` = `#c4e600` (hover), `--navy-tint` = `#33362a` (hairline on dark surfaces).
- **NEW `--ink-deep` `#16180f`** = near-black. It took over navy's **dark-surface** role: footer, closing CTA band, Growth Audit card, recognition band, `.compare-card--me`, and the `/ai-product-marketing` closing band.
- `--on-navy-mute` re-tinted bluish→warm-gray `#b7bfa4` (muted text on the near-black).
- **Lime is a FILL, never text-on-light.** `.btn-navy` / `#navbar .btn-navy` / mobile-menu CTA text → `--ink` (was `#fff`). `.btn-outline-navy` text → `--ink` (lime border kept). Both closing-band CTAs (home + AI page) were switched from `.btn-outline-navy` to solid `.btn-navy` so lime pops on the near-black.
- **Accent text on light → dark.** `.eyebrow`, `.handwritten`, `#navbar a:hover`, `.nav-cta-corner .corner-book`, `.badge-outline`, `.step-badge`, the hero funnel caption, the "need other services?" note, and the four big proof numbers ($11M+/7.35x/25%/10 days) all moved to `--ink`/`--ink-deep`. `.handwritten.light` (on dark bands) went gold→**lime** (the signature accent).
- **Hard-coded navies fixed for coherence:** `::selection` (lime bg, dark text), focus outline (`--ink-deep`), `.grid-canvas` grid lines, the nav-toggle hamburger `stroke`, and `Logo.astro`'s `bar` (`#1b2a6b`→`#16180f`, so the mark stays visible on the white navbar; reverse/white variant unchanged). The two blue-tinted inline button glows (`rgba(27,42,107,…)`) were neutralised to `rgba(22,24,15,…)`.
- **Left alone:** the hero funnel SVG's own purple→navy→teal gradient (decorative, `#1b2a6b` mid-stop) and the sticky tags (still purple/gold). Both are open options if you want to push lime further. A handful of subtle `rgba(27,42,107,…)` shadows remain in `global.css` (barely visible; low priority).

**Content refresh (all in `index.astro`, matching a client-supplied HTML paste; head/meta+schema updated in `Layout.astro`):**
- **Hero** H1 → "Stalled growth despite having paying users?"; the oversized colored subline was dropped and folded into one **body-sized** paragraph.
- **Services** H2 → "I fix the part of growth that's holding your business back."; growth-strategy + positioning-audit + GTM descriptions rewritten.
- **How it works** intro rewritten; **the step badge (`.process-num` circle) and the "Week 1–2 / Week 3 onward / Ongoing" timing labels were removed** — each card now leads with a plain "STEP 1/2/3" eyebrow (`.process-when`, margin-top zeroed). Titles → Discovery & Audit / Strategy & Execution / Measurement & Scale. `.process-num` CSS is now unused (left in place).
- **Proof** H2 → "12+ years of experience, backed by the numbers."; the $11M+ stat copy reworded.
- **About** H2 → "I help post-PMF founders engineer scalable growth."; bio p1 reworded (adds the Top 100 line). **Photo shrunk** ~470px→~260px, right/top-aligned (grid `1.55fr 0.45fr`). **Right-fit block layout revisited**: centered island → left-aligned with a "let's be honest" eyebrow; `.compare-grid` `max-width:900px` (cards ~442px). Copy on the fit/not-fit bullets tweaked.
- **Growth Audit** section H2 → "Start with a free Growth Audit."; intro reworded.
- **`Layout.astro`**: default `title` → "Fractional Head of Product Marketing | The Growth PMM"; default `description`, the Person + ProfessionalService `description`s, and `serviceType[0]` all moved to the "find the bottleneck that's capping revenue" framing.

**Still open (design):** sticky tags + funnel gradient not yet lime; the whitespace left of the shrunk About photo is open (could pull the right-fit heading up beside it). `COPY.md` is even more stale now — `.astro` files are the source of truth.

## Current state (top → bottom of `src/pages/index.astro`)

1. **Nav** — floating pill, logo + links (Free report / Services / About me) + "Book a call" (white-on-navy; a `#navbar .btn-navy` rule fixes an earlier dark-text-on-navy bug). Collapses on scroll to a persistent corner "Book a call" that carries the call through mid-page sections.
2. **Hero** — call-led.
   - Credibility tags: "Senior, fractional PMM" / "Top 100 PMM, 2025".
   - H1: "You found product-market fit. Now find what's capping your growth."
   - Meaty subtext pitching the offer: extended PMM team, a senior PMM for strategy and execution without the cost or lock-in of a full-time hire, "Product marketing, as a service."
   - Single CTA: "Book a call". (Report link and the old marker/highlighter removed from the hero.)
   - 3D funnel SVG on the right with "watch where it leaks ↓".
3. **Logo strip** — Fi Money, Practo, MakeMyTrip, Raymond, TCS.
4. **Problem ("The leak")** — "Your growth stalled for a reason. You just can't name which one yet." Ends pointing to working together ("That's where we'd start").
5. **Services** — "PMM, as a service" → "I plug in where your team needs me, starting with growth." **Growth strategy is the featured module** (`.module--featured`, "where most teams start" tag, 4-card channel grid); **Positioning audit** and **Go-to-market** sit below as secondary `.other-services` cards (condensed, no sub-grids). Modular framing, no 1-2-3 numbering.
6. **Proof** — "12+ years, and the numbers to prove it." Stat cards + "Also on record" + Recognition band.
7. **Why me (`#why-me`)** — 3-column comparison, order: full-time hire | **TheGrowthPMM** (middle, navy, "this is me" tag) | agency. Red ✗ marks for the alternatives, green ✓ for the me column. Qualitative, no prices. Stacks on mobile.
8. **About me** — first person. "I help post-PMF founders find why growth stalled, and fix it." MBA (MICA, Ahmedabad) is woven into the bio prose; the old badges and "Based in Bangalore" were removed, and there's no CTA button (the floating corner CTA covers it). Photo placeholder on right.
9. **The free Report (`#report`)** — the soft option, late on the page: eyebrow "not ready for a call yet?", H2 "Start with the free Growth Report." One navy card holds the 3-step flow AND the "What's in your report" checklist (merged; the standalone white card was removed). Report CTA still the Google Form.
10. **Closing CTA band** — "the fix is closer than you think" / "Find what's capping your growth, and start scaling again." Sells the call ("A 20-minute call… you'll leave with a clear first move"). Single CTA: Book a call (the secondary report link was removed).
11. **Footer** — links incl. FAQ; email thegrowthpmm@gmail.com, LinkedIn.

Separate page: **`/faq`** (`src/pages/faq.astro`) — NEW. Six short Q&As in a `<details>` accordion (why not full-time, how we work, cost → "book a call for a number", exit, SaaS-only, what the report is). Linked from footer + mobile menu. Kept off the homepage to keep it tight.

## Copy & voice
- **Voice:** second person ("you/your") to the reader; first person ("I") when Divya describes herself.
- **Anti-AI style guide** at `/Users/divyaabhilash/Documents/Claude/Claude Cowork/About Me/anti-ai-writing-style.md` is enforced. Notably Rule 1: max one em dash per page — there are currently **zero**; keep it that way (use periods/commas). Also killed: prose semicolons, rule-of-three padding.
- Positioning frame = **April Dunford** (alternatives → unique value → who it's for). Headlines were revisited against it.

## Funnel visual (rebuilt 2026-06-24)
- Balls are now **inline SVG `<circle>` + SMIL** (`<animateMotion>`), not CSS divs. Flow balls (translucent white) enter wide at the rim and converge to the spout, staying contained. Leak balls (coral) peel off at three different stages (Activation, Conversion, Retention) and fall out of the funnel.
- Old `.funnel-dot` / `.funnel-drip` CSS + keyframes were removed from `global.css`.

## Key decisions (don't undo without intent)
- **Call-led** (see top of file).
- Primary CTA label = **"Book a call"** (standardized; was "Book a strategy call").
- Report capture stays the existing **Google Form** for now (no Formspree, no on-site interactive quiz — both were considered and declined). Pricing stays **off the site** (call only). FAQ on its own page.
- Why-me comparison is **qualitative** (no dollar figures).
- Playful/scrapbook elements (handwritten accents, sticky tags, funnel) are intentional and used in moderation. The hero marker/highlighter was dropped; the report's "free" sticky tag and section eyebrows remain.

## Open to-dos / placeholders
- [x] Resolve **clients-per-month** contradiction — unified to "three" (2026-06-29).
- [x] Unify **brand spelling** to "The Growth PMM" incl. schema + titles (2026-06-29).
- [ ] Refresh `COPY.md` (+ the Downloads copy) to match the applied copy; they're stale.
- [ ] Replace `DIAGNOSTIC` placeholder in `index.astro` AND `faq.astro` with the real **Google Form URL** (the renamed "Growth Audit"; now only on secondary CTAs).
- [x] Real **founder photo** in About — `public/divya.jpg` added and rendering (2026-06-29).
- [x] Gate the funnel SMIL behind `prefers-reduced-motion` — done via `matchMedia` + `pauseAnimations()` (2026-06-29).
- [ ] Replace the three **`[PLACEHOLDER]` testimonials** with real client quotes or LinkedIn recommendations (biggest open trust lever).
- [ ] Add the **Google Calendar intake questions** (see the 2026-06-25 section above).
- [ ] Confirm/replace domain in `astro.config.mjs` (`site:`) + add `og-image.png` (also used by the schema `image`).
- [ ] Enable analytics (commented-out in `Layout.astro`).
- [ ] Build out the **AEO content cluster** beyond `/ai-product-marketing` (more answer-first pages: "fractional PMM vs full-time hire", "diagnosing stalled growth post-PMF", etc.). Consider adding "AI PMM" to the main nav pill, not just the footer.
- [ ] Unused CSS: `.service-row` / `.service-num` / `.service-icon` (and the old `.audit-step`) can be removed from `global.css`.
- [ ] FAQ page closing still leads with the report (intentional soft path) — revisit if you want it call-led too.

Resolved 2026-06-25: hero tags (now "Fractional Head of PMM" + "Top 100 PMM, 2025"); the `$60K` proof stat (reframed to lead with "Master of Margin", figure moved into the detail).

## Verify notes
- Use `preview_*` tools. Hero/top screenshots are reliable; deep-scroll sometimes comes back blank, so verify lower sections via DOM (`getBoundingClientRect`, computed styles).
- The ~800px preview width triggers mobile rules on a wide canvas (awkward in-between). Check real breakpoints (375 / 1280) instead.
