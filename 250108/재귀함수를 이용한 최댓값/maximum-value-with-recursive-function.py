n = int(input())
arr = list(map(int, input().split()))

def max_list(n, arr):
    for i in range(len(arr)):
        result = max(arr)
        return result

max_list(n, arr)
print(max_list(n, arr))