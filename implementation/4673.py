answer = []
for N in range(1, 10001):
    result = N
    while N != 0:
        result += (N % 10)
        N //= 10
    
    answer.append(result)

for i in range(1, 10001):
    if i not in answer:
        print(i, end=' ')