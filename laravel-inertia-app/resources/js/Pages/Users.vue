<script setup>
import { usePage } from '@inertiajs/vue3';

const { props } = usePage();
const successMessage = props.flash?.success || ''; // Verificamos si flash y success existen
</script>

<template>
    <div class="container">
        <h1>Lista de Usuarios</h1>
        <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
        <a href="/users/create" class="link">Agregar Usuario</a>
        <table border="1" class="table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Email</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="user in props.users" :key="user.id">
                    <td>{{ user.id }}</td>
                    <td>{{ user.name }}</td>
                    <td>{{ user.email }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style>
.container {
    text-align: center;
    margin-top: 50px;
}
.success-message {
    color: green;
    font-weight: bold;
    margin-bottom: 15px;
}
</style>
