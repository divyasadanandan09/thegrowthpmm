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

**Still open (design):** sticky tags + funnel gradient not yet lime; the whitespace left of the shrunk About photo is open (could pull the right-fit heading up beside it).

**`COPY.md` refreshed 2026-07-01** to match the current `.astro` copy across all three pages + global (brand name, hero, services, how-it-works steps, proof, about + right-fit block, growth-audit, FAQ, AI page). The `.astro` files stay the source of truth. The separate `~/Downloads/TheGrowthPMM-COPY.md`, if it still exists, was NOT touched and is stale.

## Update 2026-07-01 (later) — `/impeccable critique` + colorize/typeset/adapt pass

Ran `/impeccable critique` on the live site (scored **33/40 "Good"**; snapshot in `.impeccable/critique/`). Wrote a **`PRODUCT.md`** (register: brand) derived from these docs. The critique's two P1s were "the lime rebrand is only half-landed" and "lime vanishes on the light sections." Shipped fixes:

- **Colorize (commit lime fully).**
  - **Funnel retinted** from purple→navy→teal to a dark body (`#3c4a1c`→`#22271a`→`#14170e`) with **lime rim contours + lime flow balls + coral drop-off** (glow `#c4d600` top, `#ec6a43` spout). White stage labels stay readable on the dark body. Coral (`#ec6a43` balls, `#cc4117` logo dot) is now the **one deliberate supporting accent = "drop-off"**; palette is **lime + near-black + coral**.
  - **Sticky tags** → lime/near-black pair (`.purple` = lime fill/dark text, `.gold` = near-black fill/lime text; recognition-band tag switched to `.purple` so it shows on the dark band).
  - **Lime recurs on the light sections:** `.marker` retinted to lime and applied to "paying users" (hero H1) + "the numbers" (proof H2); lime "A fit if" header on the near-black card; testimonial quote-mark opacity 0.16→0.5; service icon chips unified from coral/gold/blue to pale lime `#eef6c8`.
- **Typeset.** Added **Bricolage Grotesque** as `--font-display` for `h1,h2,h3` (Inter stays for body/UI; Caveat for accents); global `letter-spacing:-0.03em` on headings (per-heading inline tracking still wins). **Thinned the handwritten kicker** — dropped on Services/Proof/Testimonials so it's no longer above nearly every section.
- **Adapt.** The floating corner "Book a call" **docks to the bottom** (`bottom:16px`) below 900px — thumb zone, no longer overlaps section headings.
- **Polish.** Funnel label "Monetisation"→"Monetization". Build compiles, zero console errors, contrast re-checked (hero body 5.0:1, purple tag 6.6:1), no mobile overflow.

**Open (deferred, not in the chosen scope):** the anonymized "Varun" lead testimonial (P3 trust — swap for a real named client); `og-image.png` + real production domain still placeholders; the `/ai-product-marketing` page still uses `.eyebrow` (uppercase) above each section (homepage-scoped critique didn't touch it).

## Update 2026-07-01 (later still) — hero copy reword + logo/favicon lime badge (client-directed)

Divya supplied new hero copy and asked to bring lime into the mark. Shipped:
- **Hero tags:** collapsed the two tags to a single **"Top 100 Global PMM, 2025"** (the "Fractional Head of PMM" tag was dropped). It's a `.sticky-tag purple` (lime fill).
- **Hero H1** → **"Unlock your next growth stage. I identify what's holding growth back and fix it."** (was "Stalled growth despite having paying users?"). Shifted from a symptom *question* to an outcome statement. The lime `.marker` moved off "paying users" onto **"holding growth back and fix it."**.
- **Hero body:** merged the two "Sometimes…" sentences into one list — "Sometimes the fix is sharper positioning, better activation, a tighter GTM, or a stronger launch." (rest unchanged).
- **Logo + favicon → lime badge.** `Logo.astro` and `public/favicon.svg` now render the funnel mark on a **lime `#DBFF00` rounded-square badge** (near-black `#16180f` funnel bars + coral `#cc4117` dot). Previously the Logo mark was a bare dark funnel with no lime; this pulls the lime fill into the wordmark on both the light nav and the dark footer. The Logo `reverse` variant no longer recolors the mark, only the wordmark (→ white); the badge is identical across variants. Favicon dropped its old navy `#1b2a6b` background.
- Verified against the live HMR server (rendered H1/tags/favicon) + `npm run build` clean; committed and deployed to Cloudflare.

## Update 2026-07-01 (even later) — hero H1 tightened, Services H2 shortened, line-wrap fixes

Divya asked for a shorter hero headline and flagged that several sub-heads/section titles were wrapping to two lines when they shouldn't. Shipped:
- **Hero H1** → **"Unlock the next growth stage."** (was "Unlock your next growth stage. I identify what's holding growth back and fix it."). The second sentence was cut; its "holding growth back and fix it" idea moved onto the Services H2 instead. The lime `.marker` now highlights **"next growth stage"**.
- **Services H2** → **"I fix what's holding your business back."** (was "I fix the part of growth that's holding your business back.").
- **Line-wrap fixes** — the wraps weren't from long copy, they were from inline `max-width`/`font-size` values that were narrower than the text needed at desktop widths:
  - Services subhead ("Most teams bring me in...") `max-width` 620px → 1050px.
  - About H2 ("I help post-PMF founders engineer scalable growth.") font-size 40px → 36px, letter-spacing -0.8px → -0.7px (its column is the narrower `1.55fr` side of the `about-grid`, not the full section width, so it needed a smaller size to fit on one line rather than a wider column).
  - Right-fit intro wrapper (`"let's be honest"` eyebrow + "Is this the right fit?" + its subhead) `max-width` 600px → 850px.
  - Verified each renders as a single line at a 1470px viewport via DOM measurement (`getBoundingClientRect` vs `lineHeight`), not just visually. The hero H1 still wraps to two lines by design (it sits in the narrower text column of the 2-col hero grid next to the funnel graphic) — that's expected, not a bug.
- Verified against a live dev server + DOM measurements; committed and deployed.

## Update 2026-07-01 (latest) — more line-wrap fixes, "three clients" highlight, logo strip audit

Divya pointed out two more subheads still wrapping to a 2nd line, asked for `only three clients a month` to get the lime `.marker` treatment, and flagged the past-experience strip's mixed text/logo styling.
- **How-it-works subhead** ("I keep it simple: diagnose the constraint...") — natural width (1359px) exceeds the full section width (1192px), so widening `max-width` alone couldn't get it to one line; dropped font-size 18px→15px (max-width 620px→1150px) so it fits on one line with room to spare. This is now visibly smaller than the other section subheads (18px) — a deliberate trade to satisfy "one line," revisit if the size mismatch reads as inconsistent.
- **Proof subhead** ("Across Fi Money, Practo, MakeMyTrip, and Raymond...") `max-width` 620px → 820px, now one line.
- **About bio**: `only three clients a month` wrapped in `.marker` (lime highlight), matching the hero/proof marker pattern.
- **Past-experience logo strip audit**: tried wiring in the existing `public/logos/tcs.svg`, but it's the full stacked "Tata Consultancy Services" lockup (Tata roundel + two lines of text) — illegible at the strip's ~22px height next to the clean Practo/MakeMyTrip wordmarks. Reverted TCS back to a text span. **Open**: need compact horizontal logo files for Fi Money, Raymond, and a simpler TCS mark before the strip can be all-logos; Divya will supply these.
- Deliberately left as-is: hero body paragraph (5 lines) and About bio paragraph (5 lines) — genuine multi-sentence body copy, not the "one-line intro" pattern; the Growth Audit section subhead (3 lines, ~240 chars) and the closing-band reassurance line (2 lines, centered) — both read as intentional short paragraphs rather than the constrained-by-accident pattern the other fixes addressed.

## Update 2026-07-01 (even later still) — hero tag swap, logo strip finished, About photo medallion

Divya supplied `fi money.svg`, `practo.png`, `raymond.png`, `tcs.jpeg` (dropped at the project root), asked whether the hero's award tag looked out of place, and asked `/impeccable polish` to redo the About photo shape.

- **Hero tag** → "Only 3 slots per month" (was "Top 100 Global PMM, 2025"). The lone award badge read oddly floating above the H1 with nothing to pair against; scarcity ties directly into the "Book a call" CTA below it and reinforces the existing three-clients-a-month positioning.
- **Past-experience logo strip, finished.** All five are now real logo `<img>`s:
  - `fi-money.svg` — the supplied icon mark, transparent bg, used as-is.
  - `raymond.png` — supplied file was white script text on a solid red background; chroma-keyed the red to transparent with Python/PIL, then recolored the preserved (text) pixels to a dark neutral (`#453e35`), since the original white fill would've been invisible against the site's light cream section background. Cropped + resized.
  - `tcs.png` (new, replaces the old unused `tcs.svg`) — supplied file was a JPEG with a white background; chroma-keyed white to transparent, cropped to content bbox, downsized to a 2x-retina-appropriate size. This is a compact horizontal `tcs` mark + "TATA CONSULTANCY SERVICES" lockup, unlike the old `tcs.svg` (the oversized stacked lockup that was illegible at strip height) — reads cleanly now.
  - The supplied `practo.png` was redundant (an already-real logo was wired in); left the existing `public/logos/practo.png` untouched.
  - Raw drop files at the project root were deleted once processed into `public/logos/`.
- **About photo → circular medallion** (`/impeccable polish`, brand register). Replaced the flat `border-radius:18px` rounded-rect with a new `.about-photo-frame` (240px circle, lime `--navy` fill as a halo ring, `box-shadow:0 20px 44px rgba(22,24,15,.22)`) wrapping `.about-photo` (circular crop via `object-fit:cover`, `object-position:50% 22%` to keep the face centered, 3px `--ink-deep` inner ring for edge definition against the light `--blue-tint` section). Mobile (`<900px`) drops to 168px, left-aligned instead of right. Chosen over an asymmetric/blob mask because it's the cleaner, more "sophisticated portrait medallion" read Divya asked for, and it reuses the existing lime-fill + dark-ring token pattern rather than introducing a new one. Verified at 1470px and ~500px viewports via the dev server.
- Verified against a live dev server; committed.

## Update 2026-07-02 — hero funnel replaced with a positioning diagram (client-directed)

Divya is taking a **different positioning route** for the hero and asked to replace the funnel graphic with a visual that *teaches* the positioning: **Product Marketing is the missing leadership function connecting Product, Sales, and Marketing after PMF.** Ran the hero framing through the LLM council first (Claude + GPT-5.2); the standing critique was that the old funnel + "Unlock the next growth stage" H1 pattern-matched to "generic growth consultant," not "senior PMM leader" — this diagram is the fix on the visual side.

**What shipped (`index.astro` hero right column + `.diagram-wrap` in `global.css`):**
- Removed the animated 3D funnel SVG **and** its `prefers-reduced-motion` SMIL-pause `<script>` (the new visual is static, nothing to pause). Renamed `.funnel-wrap` → `.diagram-wrap` (aspect-ratio `420/410`, `max-width:380px` desktop / `260px` mobile).
- **New diagram = hub-and-spoke.** Three team nodes as **fully transparent outline chips** (Product top, Sales + Marketing bottom) + thin near-black connectors converging into a central **lime "The Growth PMM" badge** (rotated -2°). This makes the *brand* the connective piece ("I am the missing function"), not the generic discipline.
- **Playful, on-brand, using the site's own vocabulary:** a **Caveat "the missing piece"** annotation with a **curly two-loop hand-drawn arrow** pointing at the hub, and a **matching Caveat caption** below ("Between product-market fit and scalable growth.") — the caption is deliberately the same handwritten voice so it reads *with* the annotation. The PMF→growth positioning now lives in that caption instead of a competing visual axis.
- **Design decisions:** dropped the enclosing **white card** (floats on the hero bg over `.grid-canvas`, more editorial); dropped the earlier "Product Marketing / The connective function" center label per Divya. **Coral is now absent from the hero** (nothing represents drop-off anymore) → the hero is pure **lime + near-black**; coral still lives lower on the page (logo dot, service icon chips). Chips are outline-only (`stroke #5f6470 @ 0.4`, no fill, no shadow).
- Iteration history this session: v1 was a white-card "PMF→Growth rail + PMM card + 3 converging teams" (two ideas at once, too busy); simplified to the hub after deciding the hub is the single ownable idea. Center text went "Product Marketing" → **"The Growth PMM"**.
- Verified on the live dev server at desktop (1440) + mobile (390), no console errors. **Not yet committed/deployed** as of this writing.

**Update (same session):** the arrow was recut so the two loops sit in the open wedge **above-right of the pill** (annotation "the missing piece" moved up to `y=120`, arrow curls down to the pill's right edge). It no longer overwrites the pill text or the annotation. The H1/copy question flagged below was then answered by the full overhaul in the next entry.

## Update 2026-07-02 (copy overhaul) — full homepage positioning rewrite (client-directed)

Divya supplied a complete new copy deck. **The homepage repositioned from "I fix your stalled growth" (which read as a generic growth consultant) to "the first Product Marketing leader you bring in before you're ready to hire a full-time one," for post-PMF B2B SaaS founders.** This is the positioning-route change the diagram entry above anticipated, now carried through the whole page. All edits in `index.astro` (+ two mobile rules in `global.css`); build clean, zero em dashes preserved.

**Hero.** H1 → "The first Product Marketing leader your company needs, before you're ready to hire one." (lime `.marker` on "before you're ready to hire one"; font 54→42px since it's longer). Added a **bold sub-line** ("You've built a product customers pay for. Now let's build predictable growth.") above the body paragraph ("I partner with post-product-market-fit B2B SaaS founders to build the positioning, messaging, GTM strategy, and cross-functional alignment that turn early traction into scalable growth, without the cost of a full-time PMM executive."). Tag, CTA, reassurance line, and the positioning diagram all unchanged.

**Two NEW sections between the logo strip and Services:**
- **Section 2 — "Growth didn't get harder. Your company got more complex."** (`background:--canvas`). Narrative: founders own everything pre-PMF, but those jobs get too interconnected to stay founder-led. A 3-up **`.ownership-row`** (Product builds / Marketing generates demand / Sales closes deals) then a lime-left-border punchline "Yet nobody owns the story that connects them. That's when growth starts slowing."
- **Section 3 — "Why founders bring me in."** (`background:--cream`). A **`.ba-table`** Before → After comparison, 5 rows (Founder owns positioning → Clear PMM ownership, etc.), white card, hairline rows, lime-agnostic (uses a "→" glyph, dark text).

**Services → "What we'll build together."** Replaced the featured-module + channel-grid + other-services structure with **four equal outcome cards** in the `.other-services` 2×2 grid: Positioning customers instantly understand / Product launches that drive adoption / Messaging that helps Sales close faster / A repeatable growth engine. The `.module--featured`, `.channel-grid`, the "where most teams start" sticky-tag, and the old Positioning-audit/GTM cards are **gone from markup** (their CSS lingers in `global.css`, now unused).

**How it works → "How we work together."** Steps rewritten: Understand your growth constraints / Build the Product Marketing foundation / Enable your team to scale. Intro trimmed.

**Other section retitles/rewrites:**
- **Proof** H2 → "The impact of 12+ years of better Product Marketing." (marker on "better Product Marketing"); subhead → "Across multiple high-growth companies like Fi Money, Practo, MakeMyTrip, and Raymond...". Stat cards unchanged.
- **Testimonials** H2 → "Trusted by founders and growth teams building their next stage of growth." (quotes unchanged; "Varun" still a placeholder).
- **About** eyebrow → "twelve years in, one lesson", H2 → "Why I do this.", copy fully rewritten to the "most companies don't struggle because they build the wrong product... that's the gap Product Marketing fills... I work with post-PMF companies as their first Product Marketing leader" story. **The old "I take only three clients a month" bio line was dropped** (scarcity now lives only in the hero tag) — re-add if you want it back in the bio. Photo medallion + right-fit block unchanged structurally.
- **Right-fit** H3 → "Are we a good fit?"; columns → "Yes, if" (5 items) / "Probably not, if" (4 items), all copy per the new deck.
- **Growth Audit** H2 → "Start with a Growth Audit." (dropped "free"); subhead rewritten to the pre-hire "focused strategy session" framing; card label "What's in your report" → "You'll walk away with" (4 items: biggest PMM gap / root cause / one first move / recommended priorities); CTA "Get your Growth Audit".
- **Closing band** eyebrow → "the honest version", H2 → "You don't need a full-time Head of Product Marketing yet. You probably do need someone thinking like one." (50→40px), sub → "Let's identify what's slowing your growth and build the Product Marketing foundation your company needs next."

**CSS:** added mobile rules `.ownership-row { grid-template-columns: 1fr }` and a `.ba-table` font tighten (`global.css`, in the `max-width:900px` block). `.other-services` already stacks on mobile, so the 4-card grid handles mobile for free.

**Verified:** `npm run build` clean; live dev server checked (hero, new sections 2/3, services, how-it-works, proof, about all render; before/after table = header + 5 rows; ownership row + punchline confirmed via DOM). Committed + pushed to `main`. **Cloudflare deploy:** if Workers Builds is git-connected (per `wrangler.jsonc`), the push auto-deploys; otherwise run `npx wrangler deploy` from an authed terminal (`wrangler login` first). The sandbox couldn't deploy (no CF token).

**Open after this pass:** nav still links only Growth Audit / Services / About (the two new sections have no nav anchors — fine, but could add); several `global.css` blocks are now dead (`.module--featured`, `.channel-grid`, `.channel-card`, plus the older `.service-row`/`.audit-step`/`.process-num`) and could be pruned; the About "three clients a month" marker line is gone (decide if it should return); `Layout.astro` title/meta/schema still say "Fractional Head of Product Marketing | The Growth PMM" and describe the old framing — **worth realigning to the new "first PMM leader" positioning** in a follow-up.

## Update 2026-07-02 (later) — critique-driven refinement + repositioning polish

A long iterative session (client-directed + two `/impeccable critique` passes). Everything below is on `main`, builds clean, detector clean. **Deploy still pending** (sandbox has no Cloudflare auth — see the deploy note at the end of the earlier 2026-07-02 entry).

**Hero visual — arrow recut.** The diagram's "the missing piece" hand-drawn arrow was overlapping the pill text; recut so the annotation + curl sit in the open wedge **above-right** of the badge. Clean now.

**Hero repositioning (client copy).**
- H1 → **"The Product Marketing leader you need, before you're ready to hire one."** (was "The first Product Marketing leader your company needs…"; lime `.marker` on "before you're ready to hire one").
- Body trimmed and de-jargoned: ICP phrase → **"post-product-market-fit startups"**, "full-time PMM executive" → **"full-time hire"**.
- Scarcity tag → **"Only 3 clients per month"** (was "slots").
- Reassurance → **"A 20-minute call. You'll leave with a clear first move."**

**Primary CTA → "Book free consultation"** (was "Book a call"), standardized on the homepage AND `/faq` + `/ai-product-marketing`. Button padding/font were tightened so the longer label reads as a slim pill, not a slab. The floating corner + mobile-menu CTAs match.

**Nav reordered + renamed → Services / Free Growth Audit / About me** (desktop pill + mobile menu; "Growth Audit" → "Free Growth Audit").

**Copy tweaks.** How-it-works H2 → "How we'd actually work." (its eyebrow dropped). Closing band H2 split: "You don't need a full-time Head of Product Marketing yet." with **"You probably do need someone thinking like one."** as a reduced-size **lime** subheading. Dropped trailing lines: Testimonials H2 → "Trusted by founders and growth teams." (dropped "building their next stage of growth"), Proof subhead dropped "Every number here is from real work.", Growth Audit subhead trimmed to one sentence, the right-fit intro line removed. Proof 7.35x stat dropped the "best contribution-margin run on record" clause.

**`/impeccable critique` #1 (scored 31/40 → after fixes, re-scored 34/40 on #2). Fixes shipped:**
- **Side-stripe border removed** (a hard AI-slop ban the detector caught) from the Section-2 punchline.
- **Services de-slopped:** the "4 identical cards" became a **featured `.module--featured` "A repeatable growth engine"** ("the outcome we build toward" tag) + a **3-up `.other-services`** grid (Positioning / Product launches / Messaging).
- **Emoji → monoline SVG icons** everywhere (Services ×4, Recognition band ×3 in lime, and later `/ai-product-marketing` ×4). All decorative icons are `aria-hidden`.
- **Section 2 mini-cards → staggered unaligned text fragments** (then removed entirely in the merge below).
- **Hero body trimmed** (see above).
- **`Layout.astro` title/meta/schema realigned** to the "Product Marketing leader you bring in before you hire a full-time one" framing (was the stale "Fractional Head of PMM / bottleneck capping revenue").
- **Proof stat labels → sentence case** (dropped `text-transform:uppercase` + tracking on the 4 category labels + "Also on record"; they were the uppercase-tracked eyebrow-tell above metrics).

**Section 3 (Before/After) polished, then merged with Section 2.**
- Polish: **arrows removed**; the **Before column is struck-through + muted**, the **After column is pale-lime + bold ink** (transformation reads from treatment, not a "→"). Repeated inline styles moved into `.ba-table` / `.ba-before` / `.ba-after` classes.
- **Merge (per critique P2):** Section 2 (complexity) and Section 3 (before/after) argued the same point back-to-back, so they're now **one section** — H2 "Growth didn't get harder. Your company got more complex." (one line at desktop) → tight lead paragraph with the lime `.marker` on "nobody owns the story that connects them" → "Here's the shift once Product Marketing has an owner." → the Before/After table. The staggered `.ownership-row` fragments and the standalone punchline block were cut (the fragments duplicated the hero diagram). `.ownership-row` CSS removed.

**Line-unwrap.** The merged H2 now sits on **one line** at desktop (removed the 820px column cap) and its lead paragraph spans full width (2 lines, not 3). Body prose elsewhere is deliberately left at readable widths.

**`/impeccable critique` #2 — secondary pages.** Critiqued `/ai-product-marketing` (29/40 pre-fix) and `/faq` (33/40). Both had drifted from the homepage's evolved system. **Fixed:** AI PMM's 4 uppercase `.eyebrow` kickers → **handwritten Caveat** kickers, its emoji → monoline SVG, and "Book a call" → "Book free consultation" on both pages. `.eyebrow` (uppercase) CSS still exists but is now **unused on every page**.

Snapshots for all three targets are in `.impeccable/critique/` (slugs `src-pages-index-astro`, `src-pages-ai-product-marketing-astro`, `src-pages-faq-astro`).

## Current state (top → bottom of `src/pages/index.astro`, refreshed 2026-07-02)

1. **Nav** — floating pill, logo (lime badge) + links (**Services / Free Growth Audit / About me**) + "Book free consultation". Collapses on scroll to a persistent corner "Book free consultation" (`#nav-cta-corner`) that docks to the bottom on mobile. Mobile menu: Services / Free Growth Audit / About me, then Proof / AI PMM / FAQ.
2. **Hero** — call-led.
   - Tag: **"Only 3 clients per month"** (`.sticky-tag purple`, lime fill).
   - H1: **"The Product Marketing leader you need, before you're ready to hire one."** (lime `.marker` on "before you're ready to hire one").
   - Bold sub-line ("You've built a product customers pay for. Now let's build predictable growth.") + a trimmed body paragraph ("I partner with post-product-market-fit startups to build the positioning, messaging, and GTM… without the cost of a full-time hire.").
   - Single CTA "Book free consultation" + reassurance "A 20-minute call. You'll leave with a clear first move."
   - **Positioning diagram** on the right: hub-and-spoke, transparent Product/Sales/Marketing outline chips converging into a lime "The Growth PMM" hub badge, Caveat "the missing piece" annotation + recut hand-drawn arrow (top-right wedge), Caveat caption "Between product-market fit and scalable growth." No white card, no coral.
3. **Logo strip** — Fi Money, Practo, MakeMyTrip, Raymond, TCS, all real logo `<img>`s.
4. **Problem → transformation (merged Sections 2+3, `--cream` bg)** — H2 "Growth didn't get harder. Your company got more complex." (one line at desktop) → lead paragraph (lime `.marker` on "nobody owns the story that connects them") → "Here's the shift once Product Marketing has an owner." → the **`.ba-table` Before → After** table (struck-through muted Before column / pale-lime bold After column, no arrows).
5. **Services (`#services`)** — handwritten kicker "the work itself", H2 "What we'll build together." A **featured `.module--featured` "A repeatable growth engine"** ("the outcome we build toward" tag) + a 3-up `.other-services` grid (Positioning customers instantly understand / Product launches that drive adoption / Messaging that helps Sales close faster). Monoline SVG icons.
6. **How it works (`#how-it-works`)** — H2 "How we'd actually work." (no eyebrow). Three steps (Understand your growth constraints / Build the Product Marketing foundation / Enable your team to scale), each a plain "STEP 1/2/3". Inline "Book free consultation" CTA.
7. **Proof (`#proof`)** — H2 "The impact of 12+ years of better Product Marketing." (marker on "better Product Marketing"), subhead "Across multiple high-growth companies like Fi Money, Practo, MakeMyTrip, and Raymond." Divided `.proof-strip` (4 stats: $11M+ / 7.35x / 25% / 10 days, **sentence-case** category labels) + "Also on record" + a near-black Recognition band (Top 100 Influencer, Master of Margin, Spot Award ×2, monoline lime icons).
8. **Testimonials (`#testimonials`)** — H2 "Trusted by founders and growth teams." Editorial: one featured lead quote ("Varun" — still a placeholder) + two real LinkedIn recs (Samarth Bhatnagar, Priyadarshi Dasgupta). Inline "Book free consultation" CTA.
9. **About + why me (`#about`)** — kicker "twelve years in, one lesson", H2 "Why I do this." Story bio (Fi Money/Practo/MakeMyTrip/Raymond, the "gap Product Marketing fills" thesis). Circular photo **medallion** on the right. **Note: the old "I take only three clients a month" marker line was dropped** (scarcity now only in the hero tag). Closes with the **"Are we a good fit?"** block: "let's be honest" kicker, H3, 2-col compare grid ("Yes, if" ✓ 5 items / "Probably not, if" ✗ 4 items).
10. **Growth Audit (`#report`)** — soft option: kicker "not ready for a call yet?", H2 "Start with a Growth Audit." Near-black card with a "You'll walk away with" list. CTA points at the `DIAGNOSTIC` Google Form **placeholder**.
11. **Closing CTA band** — kicker "the honest version", H2 "You don't need a full-time Head of Product Marketing yet." + lime subheading "You probably do need someone thinking like one." Single CTA "Book free consultation".
12. **Footer** — links incl. FAQ + AI PMM; email thegrowthpmm@gmail.com, LinkedIn.

Separate pages: **`/faq`** (`src/pages/faq.astro`) — six Q&As in a `<details>` accordion, handwritten kicker, "Book free consultation" CTA. **`/ai-product-marketing`** — the AI PMM pillar page (POV, workflows with monoline icons, guardrails, proof, 4-Q FAQ), **handwritten Caveat kickers** (was uppercase `.eyebrow`), "Book free consultation" CTA. Both linked from footer + mobile menu, both carry `FAQPage` JSON-LD.

## Copy & voice
- **Voice:** second person ("you/your") to the reader; first person ("I") when Divya describes herself.
- **Anti-AI style guide** at `/Users/divyaabhilash/Documents/Claude/Claude Cowork/About Me/anti-ai-writing-style.md` is enforced. Notably Rule 1: max one em dash per page — there are currently **zero**; keep it that way (use periods/commas). Also killed: prose semicolons, rule-of-three padding.
- Positioning frame = **April Dunford** (alternatives → unique value → who it's for). Headlines were revisited against it.

## Hero visual — history
- **2026-07-02 → positioning diagram (current).** The funnel was replaced by a static hub-and-spoke SVG (`.diagram-wrap`). See the 2026-07-02 update above for the full spec and rationale.
- **2026-06-24 → 2026-07-02: animated 3D funnel (removed).** Was inline SVG `<circle>` + SMIL `<animateMotion>` (lime flow balls converging to the spout, coral leak balls peeling off at Activation/Conversion/Retention), gated behind `prefers-reduced-motion` via a small `pauseAnimations()` script. Both the SVG and that script are gone now. The older `.funnel-dot` / `.funnel-drip` CSS was already removed back in the 2026-06-24 rebuild.

## Key decisions (don't undo without intent)
- **Call-led** (see top of file).
- Primary CTA label = **"Book free consultation"** (standardized site-wide 2026-07-02; was "Book a call", earlier "Book a strategy call").
- Report capture stays the existing **Google Form** for now (no Formspree, no on-site interactive quiz — both were considered and declined). Pricing stays **off the site** (call only). FAQ on its own page.
- **"Is this the right fit?" qualifier** (inside About, not a standalone comparison section anymore since 2026-06-30) is **qualitative** (no dollar figures).
- Playful/scrapbook elements (handwritten Caveat kickers, sticky tags, the hero positioning diagram's Caveat annotation + hand-drawn arrow, the lime `.marker` highlighter) are intentional and used in moderation. Icons are **monoline SVG, never emoji** (2026-07-02).

## Open to-dos / placeholders
- [x] Resolve **clients-per-month** contradiction — unified to "three" (2026-06-29).
- [x] Unify **brand spelling** to "The Growth PMM" incl. schema + titles (2026-06-29).
- [x] Refresh `COPY.md` to match the applied copy (done 2026-07-01, re-synced same day after the later copy/tag changes).
- [x] Real **founder photo** in About — `public/divya.jpg` added and rendering (2026-06-29); photo treatment upgraded to a circular medallion (2026-07-01).
- [x] Gate the funnel SMIL behind `prefers-reduced-motion` — done via `matchMedia` + `pauseAnimations()` (2026-06-29).
- [x] Standardize the **past-experience logo strip** to real logos for all five (2026-07-01).
- [ ] Replace `DIAGNOSTIC` placeholder in `index.astro` AND `faq.astro` with the real **Google Form URL** (the renamed "Growth Audit"; now only on secondary CTAs).
- [ ] Replace the **anonymized "Varun" lead testimonial** with a real named client quote (Samarth Bhatnagar and Priyadarshi Dasgupta are already real; Varun is the one remaining placeholder — biggest open trust lever).
- [ ] Add the **Google Calendar intake questions** (see the 2026-06-25 section above).
- [ ] Confirm/replace domain in `astro.config.mjs` (`site:` still `thegrowthpmm.pages.dev`) — Divya owns **thegrowthpmm.com** (registered at Namecheap); needs Cloudflare custom-domain setup + the `site:` swap so canonical/OG/schema URLs update. `public/og-image.png` **now exists** (was a placeholder).
- [ ] **Deploy the current `main` to Cloudflare** — many commits (2026-07-02 session) are pushed but the sandbox couldn't `wrangler deploy` (no CF auth). Run `npx wrangler deploy` from an authed terminal, or rely on Workers Builds if git-connected.
- [x] **`Layout.astro` title/meta/schema realigned** to the "Product Marketing leader you hire before a full-time one" positioning (2026-07-02).
- [x] **Secondary pages brought in line** with the homepage system (handwritten kickers, monoline icons, unified CTA) (2026-07-02).
- [x] **CTA label** revisited → changed to **"Book free consultation"** site-wide (2026-07-02).
- [ ] Enable analytics (commented-out in `Layout.astro`).
- [ ] Build out the **AEO content cluster** beyond `/ai-product-marketing` (more answer-first pages: "fractional PMM vs full-time hire", "diagnosing stalled growth post-PMF", etc.). Consider adding "AI PMM" to the main nav pill, not just the footer.
- [ ] Unused CSS to prune: `.service-row` / `.service-num` / `.service-icon`, `.audit-step`, `.process-num`, and now **`.eyebrow`** (uppercase kicker, unused everywhere since 2026-07-02) and **`.ownership-row`** (fragments removed in the section merge). Note `.module--featured` is back IN USE (Services featured card) and `.channel-grid`/`.channel-card` are IN USE on `/ai-product-marketing` — don't prune those.
- [ ] FAQ page closing still leads with the report (intentional soft path) — revisit if you want it call-led too.

## Verify notes
- Use `preview_*` tools. Hero/top screenshots are reliable; deep-scroll sometimes comes back blank, so verify lower sections via DOM (`getBoundingClientRect`, computed styles).
- The ~800px preview width triggers mobile rules on a wide canvas (awkward in-between). Check real breakpoints (375 / 1280) instead.
- **Screenshot/scroll drift (seen 2026-07-02):** `preview_screenshot` can render a viewport ~1 section *below* where `window.scrollY` reports, so scrolling to an element then screenshotting often misses it. Two reliable workarounds: (a) **DOM measurement** — `getComputedStyle` + `getBoundingClientRect` for line counts, colors, aria attrs (set the viewport to 1440 first via `preview_resize`; `window.innerWidth` confirms it, and measurements are then at desktop even though the screenshot renders narrower); (b) the **transform-scale trick** — temporarily `transform: scale(1.1–2.1)` + `transform-origin: top left` on the target section (pins it to the top-left corner so the screenshot catches it), then revert. Used both extensively this session.
