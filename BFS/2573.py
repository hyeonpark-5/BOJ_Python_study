# 2573 빙산 (bfs, 골드 4)
from collections import deque
import sys 
input = sys.stdin.readline

# 동서남북
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


# 한 사이클 돌기
def bfs(xx, yy):

    q = deque()
    q.append((xx, yy))
    visited[xx][yy] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:

                # 빙산이라면 큐
                if board[nx][ny] != 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                else:
                    # 빙산이 아니라면 바닷물
                    cnt[x][y] += 1
    return 1
    


n , m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
year = 0

while True:
    answer = []
    visited = [[0] * m for _ in range(n)]
    cnt = [[0] * m for _ in range(n)]
    
    # 빙산과 접촉되어 있는 바닷물/ 분리 확인
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and not visited[i][j]:
                answer.append(bfs(i, j))

    # 빙산 깎기
    for i in range(n):
        for j in range(m):
            board[i][j] -= cnt[i][j]
            if board[i][j] < 0:
                board[i][j] = 0

    # 길이가 0이면 모두 바다가 됨, 길이가 2 이상이면 빙산이 2개 이상으로 분리됨
    if len(answer) == 0 or len(answer) >= 2:
        break

    year += 1

if len(answer) >= 2:
    print(year)
else:
    print(0)

   



