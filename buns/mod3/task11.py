def check_winner(board):
    for row in board:
        if all(cell == 'X' for cell in row):
            return 'X'
        if all(cell == 'O' for cell in row):
            return 'O'

    for col in range(len(board)):
        if all(row[col] == 'X' for row in board):
            return 'X'
        if all(row[col] == 'O' for row in board):
            return 'O'

    if (all(board[i][i] == 'X' for i in range(len(board)))
            or all(board[i][len(board) - i - 1] == 'X' for i in range(len(board)))):
        return 'X'
    if (all(board[i][i] == 'O' for i in range(len(board)))
            or all(board[i][len(board) - i - 1] == 'O' for i in range(len(board)))):
        return 'O'
    return 'Ничья'

n = int(input("Введите размерность поля: "))
board = []
for i in range(n):
    row = list(input("Введите строку без пробелов: "))
    board.append(row)

winner = check_winner(board)
print(winner)
