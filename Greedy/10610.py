#30
n = list(input())
n.sort(reverse=True)

if n[-1] != '0':
    print(-1)
else:
    res = 0
    for i in n:
        res += int(i)
    
    if res % 3 == 0:
        print(''.join(n))
    else:
        print(-1)