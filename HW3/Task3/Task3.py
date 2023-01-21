# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def fracs_identification(list_of_numbers):
    # fracs_list = []
    # for i in range(len(list_of_numbers)):
    #     if list_of_numbers[i] % 1 != 0:
    #         fracs_list.append(round(list_of_numbers[i] % 1, 2))
    fracs_list = list(map(lambda x: round(x % 1, 2),filter(lambda x: x % 1 != 0, list_of_numbers)))
    return fracs_list

def min_value(list_of_numbers):
    min_value = list_of_numbers[0]
    for i in range(1, len(list_of_numbers)):
        if list_of_numbers[i] < min_value:
            min_value = list_of_numbers[i]
    return min_value
def max_value(list_of_numbers):
    max_value = list_of_numbers[0]
    for i in range(1, len(list_of_numbers)):
        if list_of_numbers[i] > max_value:
            max_value = list_of_numbers[i]
    return max_value

float_elements = [1.5, 1.2, 3.1, 5, 10.06]
fracs_list = fracs_identification(float_elements)
minimum = min_value(fracs_list)
maximum = max_value(fracs_list)
result = maximum - minimum

print(fracs_list)
print(result)