from collections import deque
N, K = map(int, input().split())
array = deque([i for i in range(1, N + 1)])
result = []
point = 1

while array:
    n = array.popleft()
    if point % K == 0:
        result.append(n)
    else:
        array.append(n)
    point += 1

print("<", end = '')
for i in range(N - 1):
    print(result[i], end = ', ')
print(f'{result[-1]}>')