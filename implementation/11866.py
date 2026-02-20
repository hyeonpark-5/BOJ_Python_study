# 11866 요세푸스 문제 

from collections import deque
n, k = map(int, input().split())
q = deque([i for i in range(1, n + 1)])
answer = []

while q:
    for i in range(k - 1):
        q.append(q.popleft())
    answer.append(q.popleft())

print("<" ,end= '')
for a in answer:
    if a == answer[-1]:
        print(a, end ='')
        break
    print(a, end = ', ')
print(">")