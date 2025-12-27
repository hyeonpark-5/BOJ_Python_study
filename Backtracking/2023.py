import sys
input = sys.stdin.readline

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def dfs(x):
    if x == N:
        print(int(''.join(map(str, res))))
        return

    for i in (1, 2, 3, 5, 7, 9):
        res[x] = i
        check = int(''.join(map(str, res[:x + 1])))
        if is_prime(check):
            dfs(x + 1)


N = int(input())
res = [0] * N
dfs(0)