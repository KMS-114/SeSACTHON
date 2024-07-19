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
//   server: {
//     historyApiFallback: true,
//     port: 3000,
//   },
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
    historyApiFallback: true,
  },
});
// import { defineConfig } from 'vite'
// import { svelte } from '@sveltejs/vite-plugin-svelte'

// // https://vitejs.dev/config/
// export default defineConfig({
//   plugins: [svelte()],
//     server: {
//     port: 3000,
//   },
// })