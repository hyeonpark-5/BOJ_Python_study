from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
array = [list(map(int, input())) for _ in range(n)]
board = [[0] * m for _ in range(n)]
q = deque()
q.append((0, 0))
array[0][0] = 0

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 1:
            array[nx][ny] = 0
            board[nx][ny] = board[x][y] + 1
            q.append((nx, ny))

print(board[n - 1][m - 1] + 1)