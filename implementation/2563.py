N = int(input())
array = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    
    for row in range(x, x + 10):
        for col in range(y, y + 10):
            array[row][col] = 1

answer = 0

for i in array:
    answer += i.count(1)

print(answer)