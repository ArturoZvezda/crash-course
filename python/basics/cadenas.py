# Trabajando con strings
texto = "¡Hola, Arturo!"
cadena = "Estoy aprendiendo Python"

print("Texto original:", texto)
print("En mayúsculas:", texto.upper())    # Convierte a mayúsculas
print("En minúsculas:", texto.lower())    # Convierte a minúsculas
print("Reemplazar palabras:", texto.replace("Python", "mundo"))  # Reemplaza palabras
print("¿Empieza con 'Hola'?", texto.startswith("¡Hola"))  # Verifica si empieza con algo
print("¿Termina con '!'", texto.endswith("!"))  # Verifica si termina con algo


print("Texto en diferentes formas: ", cadena,cadena.upper(),cadena.lower(),
      cadena.replace("Aprendiendo","Dominando"),cadena.startswith("Estoy"),cadena.endswith("Python"))
# Concatenación de strings
nombre = "Arturo"
apellido = "González"

nombre_completo = nombre + " " + apellido

print("Nombre completo en diferentes formas :", nombre_completo,nombre_completo.capitalize(),nombre_completo.title(),nombre_completo.swapcase(),nombre_completo.casefold())

print('''este texto
      se debe imprimir
      en multiples lineas''')