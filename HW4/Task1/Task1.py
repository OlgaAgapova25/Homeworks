# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def float_truncation(decimals, number):
    count = 1
    while decimals * 10 < 1:
        decimals *= 10
        count += 1
    num_floor = number // 1
    num_frac = number % 1
    num_frac_trunc = float(str(num_frac)[:count+2])
    number = num_floor + num_frac_trunc
    return number
def main():
    d = 0.0000001
    num = 4.1234590167891
    result = float_truncation(d, num)
    print(result)

if __name__ == "__main__":
    main()