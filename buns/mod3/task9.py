with open('data.txt', 'r') as file:
    n = int(file.readline())

def f(n):
    x, y = 0, 0
    dx, dy = 1, 1
    step_count = 1
    cur_step = 0
    for i in range(1, n + 1):
        dx = -dx
        for j in range(step_count):
            x += dx
            cur_step += 1
            if cur_step >= n:
                return x, y

        dy = -dy
        for k in range(step_count):
            y += dy
            cur_step += 1
            if cur_step >= n:
                return x, y
        step_count += 1
    return "0, 0"

with open('data.txt', 'a') as file:
    file.write('\n' + f(n))


'''for i in range (1,15):
    print(f"кол-во шагов:{i}, позиция робота:{f(i)}")'''