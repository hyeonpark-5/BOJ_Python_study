# 1018 체스판 다시 칠하기


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
answer = 2147000000

def count(x, y):
    cnt_b = 0
    cnt_w = 0

    for i in range(x , x + 8):
        for j in range(y , y + 8):
            if (i + j) % 2 == 0:
                if board[i][j] != 'W':
                    cnt_w += 1
                if board[i][j] != 'B':
                    cnt_b += 1 
            else:
                if board[i][j] == 'W':
                    cnt_w += 1
                if board[i][j] == 'B':
                    cnt_b += 1
        
    return min(cnt_w, cnt_b)

            
# 8 x 8
for i in range(n - 7):
    for j in range(m - 7):
        res = count(i, j)
        if answer > res:
            answer = res 
        
print(answer)