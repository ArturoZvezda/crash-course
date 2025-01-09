import persona

p1 = persona.Persona("Ann",32)

p1.saludar()

p2 = persona.Persona("Arturo",39)

p2.saludar()


gerente = persona.Gerente("Arturo",39,"Arquitecto de software","60000","Laboratorio de software")

gerente.mostrar_info()


print(f"En total hay {persona.Persona.contador} personas en memoria")


print(p1)
print(repr(p2))