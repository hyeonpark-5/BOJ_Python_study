# 13023 ABCDE
import sys
input = sys.stdin.readline 

def dfs(x, cnt):
    global answer
    if cnt == 4:
        answer = 1
        return
    
    for i in board[x]:
        if visited[i] != 1:
            visited[i] = 1
            dfs(i, cnt + 1)
            visited[i] = 0
        

n, m = map(int, input().split())
board = [[]  for _ in range(n)]
answer = 0

for _ in range(m):
    x, y = map(int, input().split())
    board[x].append(y)
    board[y].append(x)

for i in range(n):
    if answer == 1:
        break
    if board[i]:
        visited = [0] * n 
        visited[i] = 1
        dfs(i, 0)

print(answer)