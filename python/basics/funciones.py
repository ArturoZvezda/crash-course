import math
import mi_modulo

def saludo(nombre):
    print(f"Hola {nombre}")

def potencia(x,n=2):
    return x ** n

saludo("Arturo")

res = potencia(2,3)

print(f"El resultado de invocar potenca(2,3) es: {res}")

res = potencia(3)

print(f"El resultado de invocar potenca(3) es: {res}")

print("La raiz cuadrada de 9 es",math.sqrt(9))

print("El área de un circulo de radio 10 es",math.pi*potencia(10))

print("El factorial de 4 es",math.factorial(4))

print("El factorial de 4 usando una funcion de modulo es",mi_modulo.fac(4))

print("El factorial de un numero aleatorio usando una funcion de modulo es",mi_modulo.fac())
