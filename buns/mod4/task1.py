def check_num(nums):
    numbers = nums.split()
    numbers = [int(i) for i in numbers]

    if all(i == numbers[0] for i in numbers):
        return 'Все числа одинаковые'
    if len(numbers) == len(set(numbers)):
        return 'Все числа разные'
    return 'Есть равные и неравные числа'


n = input('Введите числа через пробел: ')
print(check_num(n))


