<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\InertiaTestController;
use App\Http\Controllers\UsersController;

use Inertia\Inertia;



/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});


Route::get('/test-inertia', [InertiaTestController::class, 'index']);

Route::get('/about', function () {
    return Inertia::render('About');
});


Route::get('/users', [UsersController::class, 'index']);

Route::get('/users/create', [UsersController::class, 'create']);
Route::post('/users', [UsersController::class, 'store']);

