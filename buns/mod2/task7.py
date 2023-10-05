"""a = input()
if a.count("1") == a.count("0"):
    print("yes")
else:
    print("no")"""
#если count нельзя юзать:
s = input()
count_0 = 0
count_1 = 0
for i in s:
    if i == '1':
        count_1 += 1
    elif i == '0':
        count_0 += 1

if count_0 == count_1:
    print("yes")
else:
    print("no")