n = int(input())
arr = [int(input()) for _ in range(n)]

max_length = 1
cnt = 1

for i in range(1, n):
    if (arr[i] > arr[i - 1]):
        cnt += 1
    else:
        max_length = max(max_length, cnt)
        cnt = 1

max_length = max(max_length, cnt)
print(max_length)