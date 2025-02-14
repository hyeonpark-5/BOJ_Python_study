X, Y = map(int ,input().split())

Z = (Y * 100) // X
start = 1
end = X
MAX = 2147000000
answer = MAX

while start <= end:
    mid = (start + end) // 2
    new = ((Y + mid) * 100) // (X + mid)
    if new > Z:
        answer = min(mid, answer)
        end = mid - 1
    else:
        start = mid + 1
   
if answer == MAX:
    print(-1)
else:
    print(answer)