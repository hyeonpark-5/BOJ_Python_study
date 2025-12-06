# 그림
import sys
sys.setrecursionlimit(10 ** 6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global res
    board[x][y] = 0
    res += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
            dfs(nx, ny)
    

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
maxx = -1 * int(10e9)

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            res = 0
            cnt += 1
            dfs(i, j)
            maxx = max(maxx, res)

print(cnt)
if maxx >= 0:
    print(maxx)
else:
    print(0)