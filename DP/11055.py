#11055 가장 큰 증가하는 부분 수열
import sys
input = sys.stdin.readline

n = int(input())
board = list(map(int, input().split()))
dp = [0] * n
dp[0] = board[0]

for i in range(n):
    for j in range(i): # 자기 자신보다 뒤
        if board[i] > board[j]:
            dp[i] = max(dp[i], dp[j] + board[i])
        else:
            dp[i] = max(dp[i], board[i])
        
print(max(dp))