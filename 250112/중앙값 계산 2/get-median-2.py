n = int(input())
arr = list(map(int, input().split()))

def medium_val(n, arr):
    result = []
    temp = []

    for i in range(n):
        temp.append(arr[i])
        temp.sort()
        if (i+1) % 2 != 0:
            result.append(temp[len(temp) // 2])
    return result        

result = medium_val(n, arr)
print(*result)