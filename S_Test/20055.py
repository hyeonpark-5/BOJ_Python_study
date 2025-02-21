from collections import deque
N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * N)
answer = 0

while True:
    answer += 1

    belt.rotate()
    robot.rotate()

    for i in range(N - 1, -1, -1):
        if i == N - 1:
            robot[i] = 0
        
        if robot[i] == 1:
            if robot[i + 1] == 0 and belt[i + 1] != 0:
                robot[i] = 0
                robot[i + 1] = 1
                belt[i + 1] -= 1
    robot[N - 1] = 0               

    if belt[0] != 0:
        robot[0] = 1
        belt[0] -= 1

    if belt.count(0) >= K:
        break

print(answer)