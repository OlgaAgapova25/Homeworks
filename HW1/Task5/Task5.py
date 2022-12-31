# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

a_x = float(input('Enter x coordinate of the point A: '))
a_y = float(input('Enter y coordinate of the point A: '))
b_x = float(input('Enter x coordinate of the point B: '))
b_y = float(input('Enter y coordinate of the point B: '))

print(round((((a_x - b_x)**2 + (a_y - b_y)**2)**0.5),2))