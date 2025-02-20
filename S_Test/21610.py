import sys
input = sys.stdin.readline

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
move = [] 
answer = 0

for _ in range(M):
    d, s = map(int, input().split())
    move.append((d - 1, s))
                
for d, s in move:
    check = set()

    while cloud:
        x, y = cloud.pop()
    
        nx = (x + (dx[d] * s)) % N
        ny = (y + (dy[d] * s)) % N
        check.add((nx, ny))
        board[nx][ny] += 1
    
    for x, y in check:
        cnt = 0
        for i in (1, 3, 5, 7):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] > 0:
                    cnt += 1

        board[x][y] += cnt

    for x in range(N):
        for y in range(N):
            if (x, y) not in check and board[x][y] >= 2:
                board[x][y] -= 2
                cloud.append((x, y))

for i in range(N):
    for j in range(N):
        answer += board[i][j]

print(answer)