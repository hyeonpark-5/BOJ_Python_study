N = int(input())

if N < 100:
    print(N)
else:
    answer = 99
    for num in range(100, N + 1):
        arr = []
        while num:
            n = num % 10
            arr.append(n)
            num //= 10
        
        check = arr[1] - arr[0]
        answer += 1
        for i in range(len(arr) - 1, 1, -1):
            if arr[i] - arr[i - 1] != check:
                answer -= 1
                break

    print(answer)