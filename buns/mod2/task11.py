num = input().replace(" ", "")
flag = False
for i in range(len(num)-1):
    for j in range(i+1, len(num)):
        if num[i] == num[j]:
            flag = True
        break
print(flag)
