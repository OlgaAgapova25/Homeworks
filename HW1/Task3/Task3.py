# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x_value = float(input('Enter x coordinate value: '))
y_value = float(input('Enter y coordinate value: '))

if x_value == 0:
    print('The point lies on Y axis')
elif y_value == 0:
    print('The point lies on X axis')
elif x_value > 0 and y_value > 0:
    print('The point lies in the I quarter')
elif x_value < 0 and y_value > 0:
    print('The point lies in the II quarter')
elif x_value < 0 and y_value < 0:
    print('The point lies in the III quarter')
else:
    print('The point lies in the IV quarter')