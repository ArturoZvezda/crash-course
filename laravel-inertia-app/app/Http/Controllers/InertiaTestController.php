<?php

namespace App\Http\Controllers;

use Inertia\Inertia;
use Inertia\Response;

class InertiaTestController extends Controller
{
    public function index(): Response
    {
        return Inertia::render('Welcome', [
            'message' => '¡Hola desde Laravel con Inertia.js!'
        ]);
    }
}
