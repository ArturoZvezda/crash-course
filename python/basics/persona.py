class Departamento:
    departamentos = ["Finanzas","IT","Comercial","Operaciones"]

class Persona:
    contador = 0

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        Persona.contador += 1
 
    @property
    def nombre(self):
        return self.__nombre.capitalize()
 
    @property
    def edad(self):
        return self.__edad
 
    @edad.setter
    def edad(self,value):
        if value < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.__edad = value
    
    def __str__(self):
        return f"Hola mi nombre es {self.nombre}"
    def __repr__(self):
        return f"Persona(nombre:{self.nombre},edad:{self.edad})"
    
    def saludar(self):
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años.")


class Empleado(Persona):
    def __init__(self, nombre, edad,puesto,salario):
        super().__init__(nombre, edad)
        self.__puesto = puesto
        self.__salario = salario
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Puesto: {self.puesto}")

    @property
    def puesto(self):
        return self.__puesto.upper()
    
    @puesto.setter
    def puesto(self,value):
        self.__puesto = value

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self,value):
        if value < 0:
            raise ValueError("El salario no puede ser negativa.")
        self.__salario = value

class Gerente(Empleado):
    def __init__(self, nombre, edad, puesto, salario,departamento):
        super().__init__(nombre, edad, puesto, salario)
        self.departamento = departamento

    @property
    def departamento(self):
        return self.__departamento.upper()

    @departamento.setter
    def departamento(self, value):
        if not value:
            raise ValueError("El departamento no puede estar vacío.")
        if value not in Departamento.departamentos:
            raise ValueError(f"El departamento no existe.")
        self.__departamento = value

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Departamento: {self.departamento}")