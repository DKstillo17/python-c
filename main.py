def Promedio(nota1,nota2,nota3,nota4):
    prom = (nota1+nota2+nota3+nota4)/4
    if prom >= 3.5:
        print(est+' Ganaste el semestre con: {}'.format(prom))
    else:
        print(est+' Perdiste el semestre con: {}'.format(prom))

print('Calculadora promedio de 4 notas')
est = input('Ingrese nombre del estudiante: ')
print('Ingrese notas para el estudiante '+est)

nota1 = float(input('¿Nota 1?'))
if nota1 >= 5.1:
    print('La nota debe ser entre 0.0 a 5.0')
    nota1 = float(input('¿Nota 1?'))

nota2 = float(input('¿Nota 2?'))
if nota2 >= 5.1:
    print('La nota debe ser entre 0.0 a 5.0')
    nota2 = float(input('¿Nota 2?'))
nota3 = float(input('¿Nota 3?'))
if nota3 >= 5.1:
    print('La nota debe ser entre 0.0 a 5.0')
    nota3 = float(input('¿Nota 3?'))
nota4 = float(input('¿Nota 4?'))
if nota4 >= 5.1:
    print('La nota debe ser entre 0.0 a 5.0')
    nota4 = float(input('¿Nota 4?'))

notas = [nota1,nota2,nota3,nota4]
#notas.append(est)
for i in notas:
    print('Nota ingresada: '+str(i))
print(Promedio(nota1,nota2,nota3,nota4))
print('Cantidad de notas ingresadas: '+str(len(notas)))

mult = int(input('Ingrese numero: '))
for n in range(1,11):
    print("{} * {} = {}".format(mult,n,mult*n))
