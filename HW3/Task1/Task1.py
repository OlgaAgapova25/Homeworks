# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
def new_list (min_number, max_number, min_value, max_value):
    if min_number > 0 and max_number > 0 and max_number > min_number and max_value > min_value:

        number_of_elements = random.randint(min_number,max_number)
        new_list = []
        for _ in range (number_of_elements):
            new_list.append(random.randrange(min_value, max_value))
    else:
        print("Error: check the arguments values")
        exit()
    return new_list

def sum_odd_indexes (your_list):
    sum = 0
    for i in range(1, len(your_list), 2):
        sum += your_list[i]
    return sum

min_number = 1
max_number = 10
min_value = -5
max_value = 5

my_list = new_list(min_number, max_number, min_value, max_value)
print(my_list)


if len(my_list) == 1:
    print("The list is too short, provide a longer list")
else:
    sum_of_odd_elements = sum_odd_indexes (my_list)
    print(sum_of_odd_elements)