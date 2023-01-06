# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def polynom_import (file_name):
    with open (f'{file_name}.txt', 'r') as file_name:
        for line in file_name:
            polynom_file_name = str(line).split(' + ')
    return polynom_file_name
def degrees_list(polynom_list):
    degrees_list = []
    for i in range(len(polynom_list)):
        degrees_list.append('')
        if '^' in polynom_list[i]:
            degrees_list[i] = int(polynom_list[i][polynom_list[i].index('^')+1:])
        elif 'x' in polynom_list[i]:
            degrees_list[i] = 1
        else:
            degrees_list[i] = 0
    return degrees_list
def coeffs_list(polynom_list):
    coefs_list = []
    for i in range(len(polynom_list)):
        coefs_list.append('')
        if '*' in polynom_list[i]:
            coefs_list[i] = int(polynom_list[i][:polynom_list[i].index('*')])
        else:
            coefs_list[i] = int(polynom_list[i])
    return coefs_list
def polynoms_sum(degrees1, degrees2, coefficients1, coefficients2):
    max_deg = max(degrees1[0], degrees2[0])
    sum_coefs = []
    sum_degrees = []
    for i in range(max_deg+1):
        sum_coefs.append(0)
        if max_deg-i in degrees1:
            sum_coefs[i] += coefficients1[degrees1.index(max_deg-i)]
    for i in range(max_deg+1):
        if max_deg-i in degrees2:
            sum_coefs[i] += coefficients2[degrees2.index(max_deg-i)]
    for i in range(max_deg+1):
        sum_degrees.append(0)
        if max_deg-i in degrees1:
            sum_degrees[i] = max_deg-i
        elif max_deg-i in degrees2:
            sum_degrees[i] = max_deg-i
    sum = ''
    for i in range(max_deg+1):
        if sum_degrees[i] > 1 and sum_coefs[i] != 0:
            sum += f'{sum_coefs[i]}*x^{max_deg-i} + '
        elif sum_degrees[i] == 1 and sum_coefs[i] != 0:
            sum += f'{sum_coefs[i]}*x + '
        elif sum_degrees[i] == 0 and sum_coefs[i] != 0:
            sum += f'{sum_coefs[i]}'
    if sum[-2] == '+':
        sum = sum[:-3]
    return sum
def main():
    polynom_list1 = polynom_import('file1')
    polynom_list2 = polynom_import('file2')
    degrees1 = degrees_list(polynom_list1)
    degrees2 = degrees_list(polynom_list2)
    coeffs1 = coeffs_list(polynom_list1)
    coeffs2 = coeffs_list(polynom_list2)
    sum = polynoms_sum(degrees1, degrees2, coeffs1, coeffs2)
    print(polynom_list1)
    print(polynom_list2)
    print(sum)
    with open('file_sum.txt', 'a') as file:
        file.write(f'{sum}\n')

if __name__ == '__main__':
    main()