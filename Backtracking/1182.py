def dfs(x, summ):
    global cnt
    if x >= N:
        return
    summ += array[x]
    if summ == S:
        cnt += 1
    
    dfs(x + 1, summ)
    dfs(x + 1, summ - array[x])

N, S = map(int, input().split())
array = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)