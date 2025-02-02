N = int(input())
array = list(map(int, input().split()))
array.sort()

start = 0
end = N - 1

check = 2147000000
result = 0

while start < end:
    ch = abs(array[start] + array[end])
    if check > ch:
        check = ch
        result = (start, end)

    if (array[start] + array[end]) > 0:
        end -= 1
    else:
        start += 1
  
print(array[result[0]], array[result[1]])