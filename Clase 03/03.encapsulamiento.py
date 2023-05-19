class Coche:
    def __init__(self, marca, color) -> None:
        self.__marca = marca  # Privado
        self._color = color  # Protegido

    def get_marca(self):  # Publico
        return self.__calcular_marca()
    
    def __calcular_marca(self):
        return self.__marca + " 2023"

coche = Coche("Toyota", "Rojo")

# print(coche.__marca)
print(coche.get_marca())