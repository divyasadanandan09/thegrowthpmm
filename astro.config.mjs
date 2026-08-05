// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

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