def check(mid):
    cnt = 1
    summ = 0
    for i in range(N):
        if summ + array[i] > mid:
            cnt += 1
            summ = array[i]
        else:
            summ += array[i]    

    return cnt

N, M = map(int, input().split())
array = list(map(int, input().split()))

start = 1
end = sum(array)
answer = 0
maxx = max(array)
while start <= end:
    mid = (start + end) // 2

    if mid >= maxx and check(mid) <= M:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)