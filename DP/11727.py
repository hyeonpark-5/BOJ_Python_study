#2xn 타일링 2
n = int(input())
board = [0] * n

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    board[0] = 1
    board[1] = 3
    board[2] = 5
    for i in range(3, n):
        board[i] = board[i - 1] + board[i - 2] * 2

    print(board[n - 1] % 10007)