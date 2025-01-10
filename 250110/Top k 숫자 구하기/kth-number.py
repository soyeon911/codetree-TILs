n, k = map(int, input().split())
nums = list(map(int, input().split()))

def asc(n, k):
    nums.sort()
    return nums[k - 1]

result = asc(n, k)
print(result)
