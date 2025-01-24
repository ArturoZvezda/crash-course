import React from 'react';
import ReactDOM from 'react-dom/client'; // Asegúrate de usar 'react-dom/client'

function ReactApp() {
    return (
        <div className="p-4 bg-yellow-100 rounded">
            <h1 className="text-xl font-bold text-yellow-600">¡React en Laravel con Vite!</h1>
            <p className="text-gray-700">Este es un ejemplo de componente React integrado con Laravel.</p>
            <button className="mt-4 px-4 py-2 bg-yellow-500 text-white rounded hover:bg-yellow-700">
                Botón React
            </button>
        </div>
    );
}

// Busca el contenedor donde se montará React
const rootElement = document.getElementById('react-app');

if (rootElement) {
    // Crea una raíz para React y renderiza el componente
    const root = ReactDOM.createRoot(rootElement);
    root.render(<ReactApp />);
}
