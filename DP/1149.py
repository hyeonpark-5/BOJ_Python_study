#1149
n = int(input())
score = []
board = [[0] * 3 for _ in range(n)]
for _ in range(n):
    r, g , b = map(int ,input().split())
    score.append([r, g, b])

board[0][0] = score[0][0]
board[0][1] = score[0][1]
board[0][2] = score[0][2]

for i in range(1, n):
    board[i][0] = min(board[i - 1][1], board[i - 1][2]) + score[i][0]
    board[i][1] = min(board[i - 1][0], board[i - 1][2]) + score[i][1]
    board[i][2] = min(board[i - 1][0], board[i - 1][1]) + score[i][2]

print(min(board[n - 1]))