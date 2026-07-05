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
  vite: {
    plugins: [tailwindcss()]
  }
});