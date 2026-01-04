# 2156 포도주 시식
import sys
input = sys.stdin.readline
n = int(input())
board = []
dp = [0] * n
for _ in range(n):
    board.append(int(input()))

dp[0] = board[0]
if n > 1:
    dp[1] = board[0] + board[1]

if n > 2:
    dp[2] = max(board[0] + board[2], board[1] + board[2], dp[1])


for i in range(3, n):
    dp[i] = max(dp[i - 2] + board[i], board[i] + board[i - 1] + dp[i - 3], dp[i - 1])

print(dp[n - 1])