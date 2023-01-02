# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = input("Enter a float number: ")
sum = 0
for i in num:
    if i.isdigit():
        sum += int(i)
print(sum)
