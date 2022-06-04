numeros = int(input('Ingrese cantidad de numeros: '))
lista = []
for i in range(numeros):
    elem = int(input('Ingrese numero: '.format(i)))
    lista.append(i)
lista.sort(reverse=True)
print(lista)



