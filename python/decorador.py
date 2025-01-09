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




saludar()