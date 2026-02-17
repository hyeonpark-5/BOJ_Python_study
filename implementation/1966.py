#1966 프린트 큐
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    check = deque()
    res = []
    cnt = 0
    document = list(map(int, input().split()))
    for i in range(n):
        check.append((document[i], i))

    while check:
        res = check.popleft()  
        flag = False

        for ch in check:
            if res[0] < ch[0]:
                flag = True
                break

        if flag:
            check.append(res)
        else:
            if res[1] == m:
                break
            cnt += 1

    print(cnt + 1)