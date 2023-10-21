def get_gsd(a, b):
    if b == 0:
        return a
    else:
        return get_gsd(b, a % b)


num1, num2 = map(int, input('Для нахождения НОД введите 2 числа через пробел: ').split())
print(get_gsd(num1, num2))
