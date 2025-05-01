N = int(input())
answer = 0
res = 0
for i in range(1, N + 1):
    answer += i
    if answer > N:
        break
    res += 1
print(res)