n = int(input())
arr = [int(input()) for _ in range(n)]

max_length = 1
curr_length = 1

for i in range(1, n):
    if (arr[i] > 0 and arr[i - 1] > 0) or (arr[i] < 0 and arr[i - 1] < 0):
        curr_length += 1
    else:
        max_length = max(max_length, curr_length)
        curr_length = 1

max_length = max(max_length, curr_length)
print(max_length)