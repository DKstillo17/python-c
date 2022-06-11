# Creamos la clase (Le colocamos parentesis cuando queremos utilizar herencia agregando dentro object)
class Carro:
    # pass no sirve pa nada solo se coloca y ya
    def __init__(self, marca, color, modelo, peso, motor):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._peso = peso
        self._motor = motor

    # Metodo GET
    @property
    def marca(self):
        return self._marca

    @property
    def color(self):
        return self._color

    @property
    def modelo(self):
        return self._modelo

    @property
    def peso(self):
        return self._peso

    @property
    def motor(self):
        return self._motor

    # Metodo SET
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @color.setter
    def color(self, color):
        self._color = color

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @peso.setter
    def peso(self, peso):
        self._peso = peso

    @motor.setter
    def motor(self, motor):
        self._motor = motor


class CarroConvertible(Carro):
    def __init__(self, marca, color, modelo, peso,motor, techo, suspension):
        super().__init__(marca, color, modelo, peso, motor)
        self._techo = techo
        self._suspension = suspension


# Almacenamos variables del objeto
carro = CarroConvertible('', '', '', '', '', 'Techo', 'suspension')

carro._marca = input('Ingrese Marca: ')
carro._color = input('Ingrese Color: ')
carro.modelo = input('Ingrese Modelo: ')
carro._peso = input('Ingrese Peso: ')
carro._motor = input('Ingrese Motor: ')
carro._techo = input('Ingrese Techo: ')
carro._suspension = input('Ingrese Tipo Suspension: ')

print(f'Carro: {carro._marca} {carro._color} {carro._modelo} {carro._peso}KG {carro._motor} {carro._techo} {carro._suspension}')
