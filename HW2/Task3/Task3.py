# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

num = 6
frac_list = []
sum = 0
for i in range(1,num+1):
    frac_list.append(round((1+1/i)**i,2))
    sum += frac_list[i-1]
print(frac_list)
print(sum)