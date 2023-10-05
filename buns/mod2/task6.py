"""a = input().split('.').reverse()
for i in range(len(a)):
    print(a[i])"""
a = input()
b = ''
for i in a[-1::-1]:
    if i == '.':
        print(b[::-1])
        b = ''
    else:
        b += i
print(b[::-1])