def is_armstrong_number(n):
    num_str = str(n)
    res = sum(int(i) ** len(num_str) for i in num_str)
    return n == res


def get_armstrong_numbers():
    n = 10
    while True:
        if is_armstrong_number(n):
            yield n
        n += 1


gen = get_armstrong_numbers()
for i in range(8):
    print(next(gen), end=' ')
