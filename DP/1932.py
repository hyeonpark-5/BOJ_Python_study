#1932
n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]

board = [[0] * i for i in range(1, n + 1)]

board[0][0] = score[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            board[i][j] = board[i - 1][j] + score[i][j]
        elif j == i:
            board[i][j] = board[i - 1][j - 1] + score[i][j]
        else:
            board[i][j] = max(board[i - 1][j - 1], board[i - 1][j]) + score[i][j]


print(max(board[n - 1]))