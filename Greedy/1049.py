n, m = map(int, input().split())
guitar = []

for i in range(m):
    x, y = map(int, input().split())
    guitar.append((x, y)) # x가 패키지 가격, y가 낱개 가격

guitar.sort(key=lambda x:(x[0], x[1]))

cal = n // 6
answer = guitar[0][0] * (cal + 1)


for i in range(m):  
    answer = min(answer, guitar[0][0] * cal + guitar[i][1] * (n % 6), guitar[i][1] * n)
    
print(answer)