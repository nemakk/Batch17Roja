'''
palabras = int(input('cuantas palabras tiene \n'))

lista = []

if palabras < 0:
    print('incorrecto')

else:
    for i in range (1, palabras + 1):
        palabra1 =  (input('poner nombres' + str(i)))
        lista.append(palabra1)
    print(lista)

palabras2 = input('palabras quieres buscar \n')

var1 = lista.count(palabras2)

print('la palabra ' + str(palabras2) + ' aparece ' + str(var1) + ' en la lista')

palabras4 = input('que palabra quieres quitar \n')

for i in lista:
    if i == palabras4:
        lista.remove(palabras4)


print('la lista actual es:', lista)

x = input('que valor quieres agregar \n')

lista1 = []

for i in range(1, x + 1)
'''

l1=[1,2,3]
l2=[4,5,6]
l3=[]

for i in range(len(l1)):
    for j in range(len(l2)):
        l3=suma(l1(i)+l2(j))

        print(l3)
