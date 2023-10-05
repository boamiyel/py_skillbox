a = input()
even_num = 0
odd_num = 0
for i in range(len(a)):
    if i % 2 == 0:
        odd_num += int(a[i])
    else:
        even_num += int(a[i])

if (odd_num + 3 * even_num) % 10 == 0:
    print("yes")
else:
    print("no")
