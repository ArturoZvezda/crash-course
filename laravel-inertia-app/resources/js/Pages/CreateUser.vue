<script setup>
import { useForm } from '@inertiajs/vue3';

const form = useForm({
    name: '',
    email: '',
});

const submit = () => {
    form.post('/users');
};
</script>

<template>
    <div class="container">
        <h1>Agregar Nuevo Usuario</h1>
        <form @submit.prevent="submit">
            <div>
                <label for="name">Nombre:</label>
                <input id="name" v-model="form.name" type="text" required />
            </div>
            <div>
                <label for="email">Email:</label>
                <input id="email" v-model="form.email" type="email" required />
            </div>
            <button type="submit">Agregar Usuario</button>
        </form>
        <a href="/users" class="link">Volver a la lista</a>
    </div>
</template>

<style>
.container {
    text-align: center;
    margin-top: 50px;
}
form {
    margin: 0 auto;
    width: 50%;
}
form div {
    margin-bottom: 15px;
}
.link {
    color: blue;
    text-decoration: underline;
    cursor: pointer;
    display: block;
    margin-top: 20px;
}
</style>
