# TheGrowthPMM — marketing site

Single-page marketing site for **Divya Sadanandan** ("TheGrowthPMM"), an independent **product marketing / growth consultant**. Built with **Astro + Tailwind v4**, but most styling is hand-authored inline styles + a custom design system in `src/styles/global.css` (CSS variables, not Tailwind utilities).

## Run / verify
- Dev server: `npm run dev` (Astro, default port 4321).
- Prefer the `preview_*` tools to verify visually. Note: in past sessions, deep-scroll screenshots sometimes came back blank — verify layout via DOM (`getBoundingClientRect`, computed styles) when screenshots are unreliable, and reserve screenshots for the hero/top of page.

## Key files
- `src/pages/index.astro` — the whole homepage (nav, hero, logo strip, problem, services, how-it-works, proof, testimonials, why-me comparison, about, the free report as a soft section, closing CTA, footer).
- `src/pages/faq.astro` — separate FAQ page at `/faq` (six Q&As in a `<details>` accordion), linked from footer + mobile menu. Carries `FAQPage` JSON-LD.
- `src/pages/ai-product-marketing.astro` — AEO / thought-leadership pillar at `/ai-product-marketing` (AI PMM point of view, the workflows, guardrails, proof, a 4-Q FAQ). The "leading voice of AI PMM" content home. Linked from footer + mobile menu. Carries `FAQPage` JSON-LD.
- `src/styles/global.css` — design system: navy palette CSS vars, `.handwritten` (Caveat accents + `.light` variant), `.sticky-tag`, `.module` (Services cards), `.channel-grid`, `.compare-*` (Why-me: alternatives get ✗, `.compare-card--me` gets ✓), `.process-*` (How it works steps), `.testimonial-lead` + `.testimonial-pair` (editorial testimonials: a featured pull-quote with an oversized Caveat quote mark, then two borderless recs under a hairline — not cards, changed 2026-06-29), `.steps-flow` + `.report-checklist` (report card), `.funnel-*`, responsive rules. (`.service-row`, `.marker`, `.audit-step` linger but are unused.)
- `src/layouts/Layout.astro` — `<head>`, fonts (Inter + Caveat), meta/OG, and the global **JSON-LD entity graph** (`Person` Divya Sadanandan + `ProfessionalService` TheGrowthPMM) emitted on every page so answer engines resolve the entity.

## Positioning & strategy (the "why", not obvious from code)
- **The site is call-led** (changed 2026-06-24; reverses the earlier lead-magnet-led approach — see `HANDOFF.md`). The primary conversion action everywhere is **booking a call**. Primary CTA text is **"Book a call"**; keep it consistent. Why: Divya takes only four clients a month, so good-fit calls beat list volume.
- The **free Growth Audit** (renamed from "Growth Report" 2026-06-26; a Google Form → personalized audit by email) is the **secondary, soft option** in the "not ready for a call yet?" section placed late on the page (after About, before the closing band). Nav link + CTAs read "Growth audit" / "Get FREE growth audit". Don't promote it back to primary without intent.
- The **hero is the pitch**, **symptom-led** (rewritten 2026-06-26). H1: "You have paying users, but growth stalled? I'll find what's capping it, and fix it." Subtext names the failure modes (positioning, an acquisition channel, activation, pricing, sales motion) and frames the offer as a fractional Head of PMM, "full-time seniority, a fraction of the cost." Tags: "Fractional Head of PMM" + "Top 100 PMM, 2025". Single CTA "Book a call" plus a reassurance line ("A 20-minute call, no pitch. You'll leave with a clear first move.").
- The **"leak" metaphor was retired site-wide** (2026-06-25). Use **"drop-off" / "where growth stalls" / "losing users" / "the constraint"** instead. The funnel visual stays (caption is now "Where are you losing users?"); don't reintroduce the word "leak" in copy.
- **CTA placement:** the floating corner "Book a call" carries the call through mid-page. Inline "Book a call" CTAs now sit in the hero, after **How it works**, after **Testimonials**, and in the closing band (added 2026-06-25 per council; this reverses the earlier "no mid-page inline CTA" rule). Services, Proof, and About keep none of their own.
- Consultancy framing = **"PMM, as a service"** (senior, embedded, fractional). Scarcity = **three clients a month** (unified across bio + comparison card, 2026-06-29).
- **ICP:** founders / CEOs / co-founders of **post-PMF startups**, funded in the last 6–12 months, with first paying customers but **stalled growth**. Copy should address them directly.
- Services are **modular, not a fixed 1-2-3 sequence** (changed 2026-06-25). **Growth strategy is the featured/hero service** (most engagements start there; keeps the 4-card channel grid: paid / organic / lifecycle / experimentation). **Positioning & messaging audit** and **Go-to-market** are presented below as secondary "other services" (condensed, no sub-grids). Framing: "I plug in where your team needs me, starting with growth," not "I do all three in order."

## Design system
- Navy `#1b2a6b` primary; **cool navy-tinted neutral backgrounds** (`--cream` #e7ebf5 cool, `--blue-tint`, white; warm beige was retired 2026-06-29 as the AI-default tell). Warmth now lives only in small accents (coral/gold icon chips, sticky tags). **Inter** for UI, **Caveat** (`.handwritten`) for playful scrapbook accents. `--warm-line` #d6dcec is the cool hairline on tinted sections.
- Playful elements (handwritten accents, rotated `.sticky-tag` notes, grid-canvas) are intentional — used in the hero tags, section eyebrows, the report card ("free" tag), closing band, and the funnel caption. Keep them tasteful, don't overdo. The `.marker` highlighter class still exists but is currently unused (dropped from the hero).
- The hero **funnel is a 3D SVG** (stacked frustums with elliptical rims + aurora purple→navy→teal gradient + cylindrical shading). Balls are animated inline via **SVG/SMIL** (`<animateMotion>`): translucent white balls flow down and converge to the spout, coral balls drop out at different stages. (Not the old CSS `.funnel-dot`/`.funnel-drip`, which were removed.)
- **Services** render as one featured `.module--featured` card (Growth strategy, with a "where most teams start" sticky-tag) plus an `.other-services` 2-up grid (Positioning audit, Go-to-market (GTM) strategy). No numbers. The **About** section closes with an **"Is this the right fit?"** qualifier block (replaced the full-time-vs-Growth-PMM comparison, 2026-06-30): a 2-column `.compare-grid` reusing the compare-card styles — navy "A fit if" card (green ✓, 4 items) + white "Not a fit if" card (red ✗, 3 items). It qualifies the ICP honestly and filters bad-fit calls. Deliberately drops a "regulated industry" disqualifier (would contradict the Fi Money/healthtech proof) and any hours/price framing.

## Copy rules
- Follow the anti-AI writing style at `/Users/divyaabhilash/Documents/Claude/Claude Cowork/About Me/anti-ai-writing-style.md`. Avoid rule-of-three padding, "not X but Y" parallelism, and empty AI-consultant eyebrow phrases.
- Every section eyebrow (handwritten) should read coherently *into* its heading, not duplicate it.
- **Voice:** second person ("you/your") to the reader; first person ("I") when Divya describes herself. Anti-AI Rule 1 is strict here — keep the page at **zero em dashes** (use periods/commas).
- Revenue/impact metrics use **$** consistently (no ₹).
- Contact email: **thegrowthpmm@gmail.com**. Brand mark: **"The Growth PMM"** (with spaces) everywhere visible — nav, footer logo + copyright, all page `<title>`s, the comparison card. The JSON-LD `ProfessionalService` uses `name: "The Growth PMM"` + `alternateName: "TheGrowthPMM"` so the one-word form still resolves (unified 2026-06-29).

## Open placeholders (must be filled before launch)
- `DIAGNOSTIC` const in `index.astro` (and `faq.astro`) = `[PLACEHOLDER: Growth Funnel Diagnostic Google Form link]` — the report's Google Form URL. Now powers the **secondary report CTAs** only.
- Founder **photo** in About is still a placeholder. One-line swap: drop a file at `public/divya.jpg` and replace the `.about-photo` div with the `<img>` in the adjacent HTML comment.
- **Booking qualification:** native Google Calendar intake questions were chosen (2026-06-25) but can't be set from code. The 3 questions + setup steps are in `HANDOFF.md`; Divya adds them in Calendar's booking form.
- `astro.config.mjs` `site:` is still `https://thegrowthpmm.com` (update if domain differs). Schema/canonical/OG URLs all derive from it.
- `og-image.png` does not exist yet (referenced by OG tags + the `Person`/`ProfessionalService` schema `image`).
- Analytics script in `Layout.astro` is commented out.

See `HANDOFF.md` for full decision log and to-dos.
