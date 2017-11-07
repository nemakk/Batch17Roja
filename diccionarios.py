diccionario={'nombre':'carlos', 'edad':22,'cursos':['python','flask']}
print(diccionario)
print(diccionario['nombre'])
print(diccionario['edad'])
print(diccionario['cursos'])

dic=dict(nombre='carlos', appellido='suarez', edad=34)
#print(dic)
for key,value in diccionario.items():
    print(key+":"+str(value))

#print('con esto agregamos elemento a la lista')
lista_cursos=diccionario['cursos']
lista_cursos.append('java')
print(lista_cursos)
print(diccionario)

print("______________________________")
#devuelve el numero de elementos que tiene el diccionario
print(len(diccionario))

print("______________________________")

#devuelve una lista con las claves del diccionario
print(diccionario.keys())

print("______________________________")

#devuelve una lista con los valores del diccionario
print(diccionario.values())

print("______________________________")

#Devuelve el vlor del elemento con su clave y si no lo encuentra
print(diccionario.get('nombre','juanito'))

#inserta un elemnto al diccionario con su clave:valor

diccionario['key']= 'value'
print(diccionario)


#Elimina el elemento por la clave
diccionario.pop('key')
print(diccionario)

#devuelve la copia de un diccionario
diccionario2=diccionario.copy()
print(diccionario2)

#Anade los elementos de un diccionario a otro
diccionario.update(dic)
print(diccionario)
