N = int(input())
rope = []
weight = 0
for _ in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)
for i in range(N):
    res = rope[i] * (i + 1)
    if weight < res:
        weight = res

print(weight)