def search(target):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return darray[target]
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

n = int(input())
array = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
array.sort()

darray = {}
for a in array:
    if a in darray:
        darray[a] += 1
    else:
        darray[a] = 1

for i in range(m):
   print(search(check[i]), end = ' ')