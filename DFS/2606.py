def dfs(v):
    global count 
    count += 1
    visited[v] = 1
    for i in range(computerNum + 1):
        if visited[i] != 1 and board[v][i] == 1:
            dfs(i)
        
computerNum = int(input())
connectNum = int(input())
board = [[0] * (computerNum+ 1) for _ in range(computerNum + 1)]
count = -1
visited = [0] * (computerNum + 1)
for i in range(connectNum):
    x, y = map(int ,input().split())
    board[x][y] = 1
    board[y][x] = 1

dfs(1)
print(count)