# A->B
a, b = map(int, input().split())
answer = 1
while b > a:
  
    if b % 2 == 0:
        b //= 2
    else:
        if str(b)[-1] != '1':
            break
        res = str(b)[:-1]
        b = int(res)
    
    answer += 1

if b==a:
    print(answer)
else:
    print(-1)