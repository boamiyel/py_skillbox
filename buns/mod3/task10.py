size = int(input("Введите размерность матрицы:"))
matrix = []
for i in range(size):
    matrix.append([j + 1 for j in range(size)])

for i in matrix:
    print(i) #исходная

print('_' * 3 * size)#просто разделитель для лучшего восприятия

for i in range(size):
    for j in range(i + 1, size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for i in matrix:
    print(i) #транспонированная