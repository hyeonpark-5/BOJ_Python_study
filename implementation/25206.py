#25206 너의 평점은

scores = {"A+":4.5, "A0": 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0,
          "D+" : 1.5, "D0" : 1.0, "F" : 0}

total = 0
res = 0

#전공평점:(학점 x 과목평점)

for _ in range(20):
    subject, num, score = input().split()
    
    if score == 'P':
        continue
    else:
        total += (float(num) * scores[score])
        res += (float(num))


print(round(total/res, 6))