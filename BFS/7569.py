#7569 토마토
import sys
from collections import deque
input = sys.stdin.readline

dx =[-1, 1, 0, 0, 0, 0]
dy =[0, 0, -1, 1, 0 ,0]
dz = [0, 0, 0, 0, 1, -1]
m, n, h = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
check = [[[0]*m for _ in range(n)] for _ in range(h)]


q = deque()

for z in range(h):
    for x in range(n):
        for y in range(m):
            if board[z][x][y] == 1 and check[z][x][y] == 0:
                q.append((z, x, y))
                check[z][x][y] = 1

while q:
    z, x, y = q.popleft()

    for i in range(6):       
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and board[nz][nx][ny] == 0:
            if check[nz][nx][ny] == 0:
                q.append((nz, nx, ny))
                board[nz][nx][ny] = board[z][x][y] + 1
                check[nz][nx][ny] = 1
                
flag = 0
day = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if board[z][x][y] == 0:
                flag = 1
            day = max(day, board[z][x][y])

if flag:
    print(-1)
else:
    print(day - 1)