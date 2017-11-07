'''
SEMAFORO = VERDE
X = VERDE
OR
c1  c2  r
1   0   1
0   1   1
1   1   1
0   0   0

AND
c1  c2  R
1   0   0
0   1   0
0   0   0
1   1   1
'''
'''
x = int(input('INGRESA LA VARIABLE X \n'))
y = int (input('INGRESA LA VARIABLE Y\n '))

if x == 3 and y == 2:
    print('SE CUMPLIO AND')
else:
    print('NO')



if x == 3 or y == 2:
    print('SE CUMPLIO OR')
else:
    print('NO')
'''
'''
x = int(input('INGRESA LA VARIABLE X \n'))
y = int (input('INGRESA LA VARIABLE Y\n '))

result = (x % y)

if result == 0:
    print('exacta')
else:
    print('no es exacta')
'''
'''
x = int(input('INGRESA LA VARIABLE X \n'))
y = int (input('INGRESA LA VARIABLE Y\n '))

if x > y:
    print('x mayor que y')
elif x < y:
    print('y menor que x')
else:
    print ('iguales')
'''

#!/usr/bin/python
#-*- coding:utf-8 -*-
'''
x = int(input('INGRESA LA VARIABLE X \n'))
y = int (input('INGRESA LA VARIABLE Y\n '))
z = int (input('INGRESA LA VARIABLE Z\n '))

if x > y > z:
    print('x mayor')
elif y > x > z:
    print('y mayor')
elif z > x  and y:
    print('z mayor')
else:
    print('todos iguales')
'''
'''
var1 = 'hola mundo'
var2 = 'python'

print(var1.upper())
print(var2.lower())

print(var2[-2])
print(var2[1:5[]])
'''

x = int(input('ingresa la variable X \n'))
y = int(input('ingresa la variable Y \n'))
z = int(input('ingresa la variable Z \n'))

if x > y and y > z:
    print(x)
elif y > x and x > z:
    print(y)
else:
    print(z)

'''
var = 'hola'

for i in var:
    print(i)
'''
x = int(input('ingresa el anio inicial \n'))
y = int(input('ingresa el anio final \n'))

result = (y-x)

if result > x:
    print('han pasado' result)
else:
    print('faltan' result 'anios para llegar al anio' x)
