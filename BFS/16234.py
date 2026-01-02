#16234 인구 이동
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def bfs(a, b):
    q = deque()
    q.append((a, b))
    c = []
    c.append((a, b))
    summ = board[a][b]
    cnt = 1
    
    while q:
        x, y = q.popleft()
     
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and L <= abs(board[x][y] - board[nx][ny]) <= R:
                if check[nx][ny] == 0:
                    q.append((nx, ny))
                    c.append((nx, ny))
                    summ += board[nx][ny]
                    cnt += 1
                    check[nx][ny] = 1

    if len(c) <= 1:
        return 0

    for xx, yy in c:
        board[xx][yy] = (summ // cnt)
    return 1

day = 0
while True:
    stop = 0
    check = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if check[i][j] == 0:
                check[i][j] = 1
                stop += bfs(i, j)
    
    if stop == 0:
        break
    day += 1

print(day)