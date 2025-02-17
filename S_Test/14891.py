from collections import deque

def left(num, direction):
    if num < 0:
        return
    if V[num][2] != V[num + 1][6]:
        left(num - 1, -direction)
        V[num].rotate(direction)

def right(num, direction):
    if num > 3:
        return
    if V[num][6] != V[num - 1][2]:
        right(num + 1, -direction)
        V[num].rotate(direction)

V = [deque(list(map(int, input()))) for _ in range(4)]
check = deque([])
count = 0
K = int(input())

for _ in range(K):
    x, y = map(int, input().split())
    check.append((x - 1, y))

for _ in range(K):
    number, dir = check.popleft()
    left(number - 1, -dir)
    right(number + 1, -dir)
    V[number].rotate(dir)


for i in range(4):
    if V[i][0] == 1:
        count += 2 **(i)

print(count)