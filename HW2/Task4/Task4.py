# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random
n = 5
n_list = []
for i in range(n):
    n_list.append(random.randint(-n, n))
with open('file.txt', 'r') as data:
    positions = []
    for line in data:
        positions.append(int(line))
production = 1
for i in range(len(positions)):
     production *= n_list[positions[i]]
print(n_list)
print(positions)
print(production)
