"""a = input().split()
ans = ''
for i in range(len(a)):
    ans = ans + a[i][-1]
print(ans)"""

a = input()
word = ""
for i in range(1, len(a)):
    if a[i] == " ":
        word += a[i-1]
print(word + a[len(a)-1])

