#2667 (bfs)
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(xx, yy):
    global cnt
    q = deque()
    q.append((xx, yy))
    board[xx][yy] = 0
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 1:
                board[nx][ny] = 0
                cnt += 1
                q.append((nx, ny))

N = int(input())
board = [list(map(int, input())) for _ in range(N)]
count = 0
result = []

for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            cnt = 1
            count += 1
            bfs(i, j)
            result.append(cnt)

result.sort()
print(count)
for res in result:
    print(res)