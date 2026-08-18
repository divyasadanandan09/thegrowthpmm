// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';
import { loadEnv } from 'vite';

// The Growth Audit quiz posts to an Apps Script webhook whose URL Astro inlines
// into the client bundle at build time. `.env` is gitignored, so on Cloudflare
// the value comes from the dashboard variable and nowhere else. When it is
// absent the quiz still builds, still scores the founder and still renders
// results, but posts nowhere: no sheet row, no email, no record of the lead.
// That happened between 2026-08-04 and 2026-08-17 and cost four completions.
//
// Fail the build instead. A deploy that stops is noticed in minutes; a deploy
// that quietly discards leads took thirteen days to spot.
//
// Only production builds are gated. `astro dev` must keep working on a fresh
// clone with no .env, and the quiz already degrades honestly there: it tells
// the founder to screenshot their results rather than promising an email.
// loadEnv, not process.env: Vite reads .env into import.meta.env and does not
// populate process.env, so a bare process.env check fails a local build that
// has the value sitting in .env. loadEnv merges both sources, which is what
// the bundle itself is compiled against.
const auditEndpoint = loadEnv(
  process.env.NODE_ENV ?? "development",
  process.cwd(),
  "PUBLIC_"
).PUBLIC_AUDIT_ENDPOINT;

if (process.env.NODE_ENV === "production" && !auditEndpoint) {
  throw new Error(
    "PUBLIC_AUDIT_ENDPOINT is not set, so the Growth Audit quiz would deploy " +
      "without a webhook and silently discard every submission.\n" +
      "Set it in Cloudflare Pages under Settings > Variables and secrets, for " +
      "the environment being built, then redeploy."
  );
}

// https://astro.build/config
export default defineConfig({
  // Served on www (apex thegrowthpmm.com does not resolve yet), so canonical/OG
  // must point at www or scrapers hit a dead image URL. 2026-07-03.
  site: "https://www.thegrowthpmm.com",
  // Honor the PORT env var (defaults to Astro's 4321) so the dev server can be
  // placed on a free port when 4321 is already taken. 2026-07-05.
  server: { port: process.env.PORT ? Number(process.env.PORT) : 4321 },
  // Astro's default 'auto' only inlines stylesheets under 4KB, so both of ours
  // shipped as separate files and BOTH blocked render: Lighthouse charged them
  // 160ms and 470ms, the latter for a 2.5KB file whose cost is almost entirely
  // the round trip. Inlining puts them in the document that is already in
  // flight. It costs the cross-page CSS cache, which is a poor trade on a site
  // where most visitors read one page. 2026-08-05.
  build: { inlineStylesheets: "always" },
  vite: {
    plugins: [tailwindcss()]
  }
});