# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
def new_list (number_of_elements, min_value, max_value):
    if number_of_elements > 0 and max_value > min_value:
        new_list = []
        for _ in range (number_of_elements):
            new_list.append(random.randint(min_value, max_value))
    else:
        print("Error: check the arguments values")
        exit()
    return new_list

# def get_super(x):
#     normal = "0123456789"
#     super_s = "⁰¹²³⁴⁵⁶⁷⁸⁹"
#     res = x.maketrans("".join(normal), "".join(super_s))
#     return x.translate(res)

def new_polynomial (degree, koefs):
    polynom_string = ''
    for i in range(degree-1):
        if koefs[i] != 0:
            polynom_string += f'{koefs[i]} * x^{degree-i} + '
    if koefs[-2] != 0:
        polynom_string += f'{koefs[-2]} * x + '
    if koefs[-1] != 0:
        polynom_string += f'{koefs[-1]}'
    return polynom_string

def main():
    k = 5
    min_value = 0
    max_value = 100
    coefficients = new_list(k+1, min_value, max_value)
    result = new_polynomial(k, coefficients)
    with open('file.txt', 'a') as file:
        file.write(f'{result}\n')
    print(result)

if __name__ == "__main__":
    main()
