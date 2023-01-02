# Реализуйте алгоритм перемешивания списка.

origin_list = [3, 5, 7, 9, 10, 23]
import random

for i in range(len(origin_list)):
    new_position = random.randint(0, len(origin_list) - 1)
    temp = origin_list[i]
    origin_list[i] = origin_list[new_position]
    origin_list[new_position] = temp
print(origin_list)

