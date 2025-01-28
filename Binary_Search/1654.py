def count(num):
    cnt = 0
    for i in range(k):
        cnt += (array[i] // num)
    
    return cnt

k, n = map(int, input().split())
maxx = -1
array = []

for _ in range(k):
    num = int(input())
    array.append(num)
    if num > maxx:
        maxx = num

start = 1
end = maxx
answer = 0

while start <= end:
    mid = (start + end) // 2
    if count(mid) >= n:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)