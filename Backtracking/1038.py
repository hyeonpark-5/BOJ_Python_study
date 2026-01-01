#1038 감소하는 수
import sys
input = sys.stdin.readline
def check(i):
    global res
    if len(res) == 1:
        return 1
    if res[-2] > i:
        return 1
    else:
        return 0
    
def dfs(x):
    global res, cnt
    if x == 10:
        return 

    for i in range(10):
        res.append(i)
        if check(i):
                cnt += 1
                dfs(x + 1)
                answer.append(int(''.join(str(i) for i in res)))
        res.pop()


n = int(input())
cnt = 0
res = []
answer = []

dfs(0)

if n >= len(answer):
    print(-1)
else:
    answer.sort()
    print(answer[n])