# 7562 (bfs)
from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]
for _ in range(T):
    I = int(input())
    board = [[0] * I for _ in range(I)]
    check = [[0] * I for _ in range(I)]
    x, y = map(int, input().split())
    xx, yy = map(int, input().split())
    board[xx][yy] = -1
    q = deque()
    q.append((x, y))
    
    if x == xx and y == yy:
        print(0)
        continue

    while q:
        x, y = q.popleft()
        if x == xx and y == yy:
            break
       
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < I and 0 <= ny < I and check[nx][ny] != 1:
                check[nx][ny] = 1
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))

    print(board[xx][yy])