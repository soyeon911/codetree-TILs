def modify(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] //= 2

n = int(input())
numbers = list(map(int, input().split()))

modify(numbers)
for j in numbers:
    print(j, end = " ")