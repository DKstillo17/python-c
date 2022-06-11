class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self, color, rueda, velocidad):
        super().__init__(color, rueda)
        self.velocidad = velocidad

vehiculo = Coche('','','')
print('Ingrese valores al coche: ')
vehiculo.color = input('Ingrese Color: ')
vehiculo.ruedas = input('Ingrese Numero de Ruedas: ')
vehiculo.velocidad = input('Ingrese Velocidad Maxima: ')
print(f'Coche: Color: {vehiculo.color} - Ruedas: {vehiculo.ruedas} - Velocidad: {vehiculo.velocidad}Km/h')
print('Registro completado del coche.')

class Bicicleta(Vehiculo):
    def __init__(self, color, rueda, tipo):
        super().__init__(color, rueda)
        self.tipo = tipo


vehiculo = Bicicleta('', '', '')
print('Ingrese valores de la bicicleta: ')
vehiculo.color = input('Ingrese Color: ')
vehiculo.ruedas = input('Ingrese Numero de Ruedas: ')
vehiculo.velocidad = input('Ingrese Tipo: ')
print(f'Bicicleta: Color: {vehiculo.color} - Ruedas: {vehiculo.ruedas} - Tipo: {vehiculo.tipo}')
print('Registro completado de bicicleta.')
