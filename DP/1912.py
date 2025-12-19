# 연속합
n = int(input())

score = list(map(int, input().split()))
board = [0] * n
board[0] = score[0]

for i in range(1, n):
    board[i] = max(score[i], board[i - 1] + score[i])

print(max(board))