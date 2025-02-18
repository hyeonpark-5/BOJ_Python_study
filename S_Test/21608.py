import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
N = int(input())
room = [[0] * N for _ in range(N)]
student = {}
score = [0, 1, 10, 100, 1000]
answer = 0
for _ in range(N ** 2):
    P = list(map(int, input().split()))
    student[P[0]] = P[1:]
    
for name in student.keys():

    check = []
    for x in range(N):
        for y in range(N):

            if room[x][y] != 0:
                continue
            
            count = 0
            people = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if room[nx][ny] in student[name]:
                        people += 1
                    elif room[nx][ny] == 0:
                        count += 1
                    else:
                        None
      

            check.append((x, y, people, count))

    check.sort(key=lambda x:(-x[2], -x[3], x[0], x[1]))
    room[check[0][0]][check[0][1]] = name
    
    
for x in range(N):
    for y in range(N):
        cnt = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if room[nx][ny] in student[room[x][y]]:
                    cnt += 1
        
        answer += score[cnt]

print(answer)