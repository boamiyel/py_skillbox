def get_num_pow(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return get_num_pow(a, n // 2) * get_num_pow(a, n // 2)
    else:
        return a * get_num_pow(a, n - 1)


num, num_pow = map(int, input('Введите число и его степень через пробел: ').split())
print(get_num_pow(num, num_pow))
