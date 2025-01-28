def check(num):
    cnt = 0
    for i in range(N):
        if array[i] <= num:
            cnt += array[i]
        else:
            cnt += num
    
    return cnt

N = int(input())
array = list(map(int, input().split()))
array.sort()
M = int(input())
answer = 0
start = 1
end = array[-1]

while start <= end:
    mid = (start + end) // 2
    res = check(mid)
    if res <= M:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
    