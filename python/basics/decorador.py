def mi_decorador(func):
    print("inicio decorador")
    def wrapper():
                print("antes...")
                func()
                print("despues...")
    print(func())
    return wrapper


@mi_decorador
def saludar():
        print("hola mundo")
        return "retorno de hola mundo"


def mi_decorador(func):
    def wrapper():
        print("Antes de ejecutar la función")
        func()
        print("Después de ejecutar la función")
    return wrapper

saludar()

# Decorador básico


# Aplicamos el decorador
@mi_decorador
def mi_funcion():
    print("¡Ejecutando la función principal!")

# Probamos la función decorada
mi_funcion()

saludar()