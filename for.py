'''
var = 'hola'

for i in range (52,100):
    print(i)
print(acabe)
'''
'''
print ('multiplo de dos')
cuenta= 0
for i range(1,100)
    if i % 2 == 0:
        cuenta = cuenta + 1

print(cuenta)

print ("acumulador")
suma = 0
for i in range (1,4):
    suma = suma + i
    print ('resultado', suma)
'''
'''
print ('multiplo de dos')
cuenta= 0
for i in range(0,1000):
    print(i)
'''
'''
print ('multiplo de dos')
cuenta= 0
for i in range(0,1000):
    if i % 2 == 0:
        print(i)
'''
'''
var = "ELEFANTE"
cuenta= 0
for i in var:
    if i == "E":
        cuenta = cuenta + 1
    if cuenta == 3:
        print('esta es la tercera')
'''

x = int(input('ingresa cantidad de articulos \n'))
y = int(input('ingresa el costo por articulo \n'))

result = y
result2= (y -(y*.05)) * x
result3= ((y*x)*.05)

if x <= 5:
    print(result)
elif x>=5:
    print('el costo total es', result2, 'el descuento fue de:', result3)
