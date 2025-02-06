<?php

namespace App\Http\Controllers;

use Inertia\Inertia;
use Illuminate\Http\Request;

class UsersController extends Controller
{
    private $users = [
        ['id' => 1, 'name' => 'Juan Pérez', 'email' => 'juan@example.com'],
        ['id' => 2, 'name' => 'María García', 'email' => 'maria@example.com'],
        ['id' => 3, 'name' => 'Carlos López', 'email' => 'carlos@example.com'],
    ];

    public function index()
    {
        return Inertia::render('Users', [
            'users' => $this->users,
        ]);
    }

    public function create()
    {
        return Inertia::render('CreateUser');
    }

    public function store(Request $request)
    {
        // Validar los datos enviados
        $validated = $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|email|max:255',
        ]);

        // Simular almacenamiento (puedes usar una base de datos real aquí)
        $newUser = [
            'id' => count($this->users) + 1,
            'name' => $validated['name'],
            'email' => $validated['email'],
        ];

        // Agregar el nuevo usuario a la lista simulada
        $this->users[] = $newUser;

        // Redirigir con un mensaje de éxito
        return redirect('/users')->with('success', 'Usuario agregado exitosamente.');
    }
}
