edad = 10


if edad >= 18:
    print("Hola, eres mayor de edad")
elif edad >=13:
    print("Hola, eres adolescente")
else:
    print("Hola, eres menor de edad")



cadena = "Hello World!"

for numero in range(1,len(cadena)):
    print("Caracter #",numero,"de",cadena,cadena[numero-1])

caracter = 0

while cadena[caracter] != '!':
    print("El caracter es",cadena[caracter])
    caracter += 1

caracter = 0

while cadena[caracter] != ' ':
    print(caracter,"caracteres sin encontrar un espacio")
    caracter += 1

caracter = 0

while caracter > len(cadena):
    if cadena[caracter] == ' ':
        print(cadena[caracter])
    else:
        print("Encontré un espacio")
        break

for numero in range(0,len(cadena)):
    if cadena[numero] != ' ':
        print(cadena[numero])
    else:
        continue


caracter = 0
length = 0

try:
    while cadena[caracter]:
        length +=1
        caracter +=1
except IndexError:
    print("El tamaño de la cadena es",length)
    

foodies = ["enchiladas","pizza","curry"]

for food in foodies:
    print(food,"es una de mis comidas favoritas")

dimensiones = ("ancho","alto","largo")

num = 0

while num < len(dimensiones):
    print(dimensiones[num],"es una dimension")
    num += 1

personales = {"Nombre":"Arturo","Edad":39,"Estatura":1.60}

cubo = {dimensiones[0]:10,dimensiones[1]:10,dimensiones[2]:10}


for dimension in dimensiones:
    print(dimension,':',cubo[dimension])


print("Mi información personal es:")
for dato in personales:
    print(dato,':',personales[dato])

n = 0

for x in ( 2.5 for _ in "Arturo"):
    n += x

print("La expresion iteradora dio: ",n)


print(sum(1 for _ in "Hola mundo con python"),"es la cantidad de caracteres en la frase 'Hola mundo con python'")