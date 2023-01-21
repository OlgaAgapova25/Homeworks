# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

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

def nonrepeat_elements(any_list):
    list_of_els = []
    for el in any_list:
        if el not in list_of_els:
            list_of_els.append(el)
    count_els = []
    # for i in range(len(list_of_els)):
    #     count_els.append(0)
    #     for j in range(len(any_list)):
    #         if any_list[j] == list_of_els[i]:
    for i, elem_i in enumerate(list_of_els):
        count_els.append(0)
        for j, elem_j in enumerate(any_list):
            if elem_j == elem_i:
                count_els[i] += 1
    # nonrep_els = []
    # for i in range(len(count_els)):
    #     if count_els[i] == 1:
    #         nonrep_els.append(list_of_els[i])
    nonrep_els = list(filter(lambda x: x[0] == 1, list(zip(count_els, list_of_els))))

    return nonrep_els

def main():
    min_num = 4
    max_num = 20
    min_val = 1
    max_val = 10
    my_list = new_list(min_num, max_num, min_val, max_val)
    print(my_list)
    print(nonrepeat_elements(my_list))


if __name__ == "__main__":
    main()
