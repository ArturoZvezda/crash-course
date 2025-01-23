import './bootstrap';
import '../css/app.css';


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
