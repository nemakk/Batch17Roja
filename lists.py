'''
list1 = [2,3,1,4,5]
list2 = ['A','B','C','D','E']
list3 = ['MATEMATICAS', 'HISTORIA',1999, 8993]
list4 = [list1, list2, list3]
print(list1)
print(list2)
print(list3)
print(list4)


frutas = ['naranja', 'manzana', 'pera', 'fresas', 'banana', 'manzana']
print(frutas)

frutas.append('uva')
print('append')
print(frutas)

#frutas.extend(list2)
#print(frutas)


frutas.insert(0,'melon')
print('insert1')
print(frutas)

frutas.pop(3)
print('pop')
print(frutas)

frutas.remove('manzana')
print('remove')
print(frutas)

frutas.reverse()
print("reverse")
print(frutas)

frutas.sort(reverse = True)
print('sort')
print(frutas)

print('count')
frutas.count('manzana')

print(frutas.count('manzana'))

print('index')
print(frutas.index('naranja'))

print('index')
print(frutas.index('fresas',0))

for i in frutas:
    if i == "manzana":
        print("Manzana")

for i in range (0,100):
        print(i)



listx = [4,76,3,12,65,3]
listy = [234,222,523,65]

listok = listx + listy

print(listok)


list = []
for i in range (0,100):
    list.append(i)

    print(list)
'''
numero = int(input('ingresa numero \n'))

for i in range(1,11):
    numero.append(numero * i)
print (numero)
