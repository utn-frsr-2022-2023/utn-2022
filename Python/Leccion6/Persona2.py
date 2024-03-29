class Persona2:
    def __init__(self, nombre, apellido, edad):  # Encapsulamiento
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # decoradores
    def nombre(self):  # Método Getter
        print('Estamos utilizando el método get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Método Setter
        print('Estamos utilizando el método set')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')


if __name__ == '__main__':
    persona1 = Persona2('Homer', 'Simpson', 37)
    print(persona1.nombre)  # Llamada método getter
    persona1.nombre = 'Bart Simpson'  # Llamada método setter
    print(persona1.nombre)
    print(persona1.mostrar_detalles())  # Llamada al método mostrar_detalles
    # read-only porque no tiene el método set
    print(persona1.edad)

    # 1
    persona2 = Persona2('Marge', 'Simpson', 35)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Margory'
    persona2.apellido = 'Simpson'
    persona2.edad = 28
    print(persona2.mostrar_detalles())

    # 2
    persona3 = Persona2('Lisa', 'Simpson', 15)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Maggie'
    persona3.apellido = 'Simpson'
    persona3.edad = 3
    print(persona3.mostrar_detalles())

    # 3
    persona4 = Persona2('Abe', 'Simpson', 75)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Herb'
    persona4.apellido = 'Powell'
    persona4.edad = 40
    print(persona4.mostrar_detalles())
    print(__name__)