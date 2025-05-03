N = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

money = city[0]
res = road[0]
answer = 0
for i in range(1, N - 1):
    if money > city[i]:
        answer += (money * res)
        money = city[i]
        res = road[i]
    else:
        res += road[i]

answer += (money * res)
print(answer)