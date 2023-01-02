# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = 45
new_list = []
count = 0
while num / 2 >= 1:
    new_list.append(num % 2)
    num //= 2
    count += 1
new_list.append(1)
result = 0
for i in range (1,len(new_list)+1):
    result += new_list[-i]*10**(count-i+1)
print(result)