// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: "https://thegrowthpmm.com", // live custom domain (Cloudflare), 2026-07-03
  vite: {
    plugins: [tailwindcss()]
  }
});