import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, d):
    global count
    if room[x][y] == 0:
        room[x][y] = 2
        count += 1

    check = False
    for _ in range(4):
        d = (d + 3) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        if room[nx][ny] == 0:
            dfs(nx, ny, d)
            check = True
            return
   
    if check == False:
        nx = x - dx[d]
        ny = y - dy[d]
        if room[nx][ny] != 1:
            dfs(nx, ny, d)
 
    
N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
board = [[0] * N for _ in range(M)]
count = 0

dfs(r, c, d)
print(count)