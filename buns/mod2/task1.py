"""a, b = map(int, input().split())
print(a % b)"""
#без сплита🥲:
s = input()
num = ""
num_1 = 0
for i in range(len(s)):
    if s[i] != ",":
        num = num + s[i]
    else:
        num_1 = int(num)
        num = ''
print(num_1 % int(num))


