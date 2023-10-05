"""a, b, c = map(int, input().split())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(b)
"""
s = input()
n = ''
a = 0
b = 0
flag = 0
for i in range(len(s)):
    if s[i] != ' ':
        n = n + s[i]
    else:
        if flag == 0:
            a = int(n)
            flag += 1
            n = ''
        else:
            b = int(n)
            n = ''
c = int(n)

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(b)





