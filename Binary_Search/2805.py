def check(mid):
    cnt = 0
    for i in range(N):
        n = tree[i] - mid
        if n > 0:
            cnt += n

    return cnt

N, M = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()
answer = 0

start = 1
end = tree[-1]

while start <= end:
    mid = (start + end) // 2
    if check(mid) >= M:
        answer = mid
        start = mid + 1   
    else:
        end = mid - 1

print(answer)