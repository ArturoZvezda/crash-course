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

        <h1 class="text-3xl font-bold text-blue-600">¡Laravel y Tailwind CSS funcionando juntos!</h1>
        <p class="mt-4 text-gray-600">Este texto está estilizado con Tailwind CSS.</p>
        <button class="mt-6 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-700">
            Botón con Tailwind
        </button>


        <h1>¡Laravel y Livewire funcionando juntos!</h1>
        <p class="mt-4 text-gray-600">Este contador es un componente de livewire.</p>

        <livewire:counter />



        <div id="app" class="max-w-2xl mx-auto bg-gray-100 p-4">
            <h1>JavaScript dinámico</h1>
            <!-- Aquí se inyectarán los elementos dinámicos de JS -->
        </div>

        <div id="vapp" class="max-w-2xl mx-auto bg-white p-4 mt-4">
            <h1>Componente Vue</h1>
            <!-- Aquí se montará Vue -->
            <hello-world></hello-world>
        </div>

        <div id="react-app" class="max-w-2xl mx-auto bg-yellow-50 p-4 mt-4">
            <!-- Aquí se montará React -->
        </div>

        @livewireScripts

    </body>
</html>
