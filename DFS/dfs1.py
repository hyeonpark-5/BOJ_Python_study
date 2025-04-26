# 부분 집합합
def dfs(x):
    if x == n + 1:
        for i in range(1, n + 1):
            if result[i] == 1:
                print(i, end=' ')
        print()
    else:
        result[x] = 1
        dfs(x + 1)
        result[x] = 0
        dfs(x + 1)


n = int(input())
result = [0] * (n + 1)
dfs(1)