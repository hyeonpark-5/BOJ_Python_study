n = input()
num = n.split('-')
number = []
for i in num:
    result = 0
    for j in i.split('+'):
        result+= int(j)
    number.append(result)

if len(number) == 1:
    print(number[0])
else:
    answer = number[0]
    for i in range(1, len(number)):
        answer -= number[i]
    print(answer)
