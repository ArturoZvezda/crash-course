import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';
import vue from '@vitejs/plugin-vue';
import react from '@vitejs/plugin-react';
import { resolve } from 'path';

export default defineConfig({
    plugins: [
        laravel({
            input: ['resources/css/app.css', 'resources/js/app.js'],
            refresh: true,
        }),
        vue(),
        react(),
    ],
    resolve: {
        alias: {
            vue: resolve(__dirname, 'node_modules/vue/dist/vue.esm-bundler.js'),
        },
    },
});
