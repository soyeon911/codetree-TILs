n = int(input())
nums = list(map(int, input().split()))

nums.sort()

sums = []
for i in range(n):
    sums.append(nums[i] + nums[-(i+1)])

result = max(sums)
print(result)
