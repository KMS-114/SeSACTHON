// import { defineConfig } from 'vite';
// import { svelte } from '@sveltejs/vite-plugin-svelte';

// export default defineConfig({
//     plugins: [svelte()],
//     css: {
//         preprocessorOptions: {
//             less: {
//                 javascriptEnabled: true,
//             },
//         },
//     },
// });

import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
  plugins: [svelte()],
  build: {
    outDir: 'public/build',
  },
  server: {
    port: 3000,
  },
});