n = int(input())
nums = list(map(int, input().split()))

def asc_dec(arr, idx = 0):
    if idx == len(arr) - 1:
        return arr[idx]
    arr1 = sorted(arr)
    arr2 = sorted(arr, reverse = True)
    return arr1, arr2

arr1, arr2 = asc_dec(nums)

print(*arr1)
print(*arr2)
