# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime_check(k):
    prime_check_sum = 0
    for number in range(2,k):
        if k % number == 0:
            prime_check_sum += 1
        else:
            prime_check_sum += 0
    if prime_check_sum > 0:
        return 0
    else:
        return 1

def prime_multipliers(n):
    prime_div_list_to_check = []
    for num in range(2, n+1):
        if prime_check(num) == 1:
            prime_div_list_to_check.append(num)

    prime_div = [1]
    for item in prime_div_list_to_check:
        if n % item == 0:
            prime_div.append(item)
    return prime_div

def main():
    n = int(input("Enter an integer: "))
    print(prime_multipliers(n))

main()