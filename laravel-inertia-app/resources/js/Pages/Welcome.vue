<script setup>
defineProps({
    message: String
});
</script>

<template>
    <div class="container">
        <h1>Bienvenido a Inertia.js</h1>
        <p>{{ message }}</p>
        <a href="/about" class="link">Ir a Acerca de Nosotros</a>
        <a href="/users" class="link">Ver lista de usuarios</a>

    </div>
</template>

<style>
.container {
    text-align: center;
    margin-top: 50px;
}
.link {
    color: blue;
    text-decoration: underline;
    cursor: pointer;
}
</style>
