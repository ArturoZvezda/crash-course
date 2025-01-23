<template>
    <div class="p-4 bg-green-100 rounded shadow">
        <h1 class="text-xl font-bold text-green-700">¡Hola desde Vue!</h1>
        <p class="text-gray-700">Este es un componente Vue funcionando con Laravel y Vite.</p>
        <button @click="count++" class="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-700">
            Haz clic {{ count }} veces
        </button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            count: 0,
        };
    },
};
</script>

<style scoped>
h1 {
    font-size: 2rem;
}
</style>
