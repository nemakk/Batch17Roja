
'''x = int(input('ingresa el anio inicial \n'))
y = int(input('ingresa el anio final \n'))
mensaje = 'faltan'
men2 = 'han pasado '
men3 = ' anios desde el anio'
men1 = 'anios para llegar al anio'

result = (y-x)
result2 = (x-y)

if result > x:
    print('han pasado', result,'anios desde el anio', x)
elif result < x:
    print('faltan', result2, 'para llegar al anio', x)
else:
    print('estas en el anio', x)
'''
x = int(input('ingresa horario de entrada \n'))
y = int(input('ingresa horario de salida \n'))
z = int(input('ingresa cantidad de unidades \n'))

if x >= 0 AND y <= 8:
    print('jornada 3')
elif x >= 0 AND y >=8:
    print('jornada 4')
else:
    print('ingresa datos nuevamente')
