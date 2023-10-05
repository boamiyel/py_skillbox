"""a = int(input())
if a > 0:
    print(bin(a)[2:], oct(a)[2:], hex(a)[2:])
else:
    print("Неверный ввод")"""
#если нельзя их использовать, то:
num1 = int(input())
def func(num, num_sys):
    num = num1
    st = ''
    while num > 0:
        s = num % num_sys
        if s > 9:
            let = s - 10
            s = chr(ord('A') + let)
        st = str(s) + st
        num = num // num_sys
    return (st)

if num1 > 0:
    print(func(num1, 2), func(num1, 8), func(num1, 16))
else:
    print("Неверный ввод")



