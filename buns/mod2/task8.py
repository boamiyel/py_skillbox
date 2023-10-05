s, i = map(str, input().split())
counter = 0
for j in range(len(s)):
    if s[j] == i:
        counter += 1
    else:
        break
print(counter)
