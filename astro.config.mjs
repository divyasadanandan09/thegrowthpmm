// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: "https://thegrowthpmm.pages.dev", // update to the custom domain once you have one
  vite: {
    plugins: [tailwindcss()]
  }
});