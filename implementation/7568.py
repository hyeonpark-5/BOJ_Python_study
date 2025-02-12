N = int(input())
array = []
result = []
for _ in range(N):
    x, y = map(int, input().split())
    array.append((x, y))

for i in range(N):
    summ = 0
    for j in range(N):
        if (array[i][0] < array[j][0]) and (array[i][1] < array[j][1]):
            summ += 1
    
    result.append((1 + summ))

for answer in result:
    print(answer, end = ' ')