<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{{ config('app.name') }}</title>
        @vite(['resources/css/app.css', 'resources/js/app.js'])
        @livewireStyles

    </head>
    <body>
        <div id="app">
            <h1>¡Laravel y Vite funcionando juntos!</h1>
        </div>

        <h1 class="text-3xl font-bold text-blue-600">¡Laravel y Tailwind CSS funcionando juntos!</h1>
        <p class="mt-4 text-gray-600">Este texto está estilizado con Tailwind CSS.</p>
        <button class="mt-6 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-700">
            Botón con Tailwind
        </button>


            <h1>¡Laravel y Livewire funcionando juntos!</h1>
        <p class="mt-4 text-gray-600">Este contador es un componente de livewire.</p>


        <livewire:counter />

        @livewireScripts

    </body>
</html>
