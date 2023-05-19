# Definición de la clase "Persona"
class Persona:
    # Constructor de la clase
    def __init__(self, nombre):
        self.nombre = nombre + " Perez"
        nombre = ""
        print("Se ha creado una persona llamada", self.nombre)

persona_1 = Persona("Juan")
