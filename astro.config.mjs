// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  // Served on www (apex thegrowthpmm.com does not resolve yet), so canonical/OG
  // must point at www or scrapers hit a dead image URL. 2026-07-03.
  site: "https://www.thegrowthpmm.com",
  vite: {
    plugins: [tailwindcss()]
  }
});