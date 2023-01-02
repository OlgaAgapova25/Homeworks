# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

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

def pairs_production(your_list):
    if len(your_list) == 0:
        print("The list is too short, provide a longer list")
    else:
        pairs_production = []
        for i in range(len(your_list) // 2):
            pairs_production.append(your_list[i]*your_list[len(your_list) - 1 - i])
        if len(your_list) % 2 == 1:
            pairs_production.append((your_list[len(your_list) // 2])**2)
    return pairs_production

min_number_of_elements = 3
max_number_of_elements = 10
min_value = 1
max_value = 10
my_list = new_list(min_number_of_elements, max_number_of_elements, min_value, max_value)
print(my_list)

pairs_prod = pairs_production(my_list)
print(pairs_prod)

# from HW3.Task1.Task1 import new_list
#
# def pairs_production(your_list):
#     if len(your_list) <=1:
#         print("The list is too short, provide a longer list")
#     else:
#         pairs_production = []
#         for i in range(len(your_list) // 2):
#             pairs_production.append(your_list[i]*your_list[len(your_list) - 1 - i])
#     return pairs_production
#
# min_number_of_elements = 3
# max_number_of_elements = 10
# min_value = 1
# max_value = 10
# my_list = new_list(min_number_of_elements, max_number_of_elements, min_value, max_value)
# print(my_list)
#
# pairs_prod = pairs_production(my_list)
# print(pairs_prod)
