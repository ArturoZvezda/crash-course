import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';

console.log('NODE_ENV:', process.env.NODE_ENV);

export default defineConfig({
    plugins: [
        laravel({
            input: ['resources/css/app.css', 'resources/js/app.js'],
            refresh: true,
        }),
    ],
});
