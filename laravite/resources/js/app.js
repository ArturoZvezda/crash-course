import './bootstrap';
import '../css/app.css';
import { createApp } from 'vue';
// Importa un componente Vue básico (lo crearemos en el siguiente paso)
import HelloWorld from './components/HelloWorld.vue';
import './components/ReactApp'; // Importamos React


// Añade algo dinámico al DOM
const app = document.querySelector('#app');
if (app) {
    app.innerHTML += '<p>¡Este contenido fue agregado dinámicamente con JavaScript y Vite!</p>';
}

// Ejemplo básico de interacción
document.addEventListener('DOMContentLoaded', () => {
    const button = document.createElement('button');
    button.textContent = 'Haz clic aquí';
    button.onclick = () => alert('¡Hola desde JavaScript!');
    app?.appendChild(button);
});

// Crea la instancia de Vue y registra el componente
const vapp = createApp({});
vapp.component('hello-world', HelloWorld);

// Monta Vue en un contenedor con el ID `#app`
vapp.mount('#vapp');
