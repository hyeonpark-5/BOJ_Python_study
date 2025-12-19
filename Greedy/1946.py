#신입 사원
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    check = []
    answer = 1
    for _ in range(n):
        x, y = map(int, input().split())
        check.append((x , y))
    
    check.sort(key=lambda x:(x[0], x[1]))

    res = check[0][1]
    for i in range(1, n):
        if res > check[i][1]:
            answer += 1
            res = check[i][1]
        
    print(answer)