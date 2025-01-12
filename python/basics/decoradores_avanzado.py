def mi_decorador(func):
        def wrapper(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado + " decorado "
        return wrapper

def decorador_con_argumentos(mensaje):
    return mi_dec.orador

@decorador_con_argumentos("¡Esto se imprime antes de ejecutar la función!")
def saludar(nombre):
    print(f"Hola, {nombre}!")
    return nombre




@mi_decorador
def greeting(name):
    print(name)
    return name

# Llamamos a la función decorada
print(saludar("Mundo"))

greeting("Arturo")
