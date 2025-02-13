n, t = map(int, input().split())
arr = list(map(int, input().split()))

max_length = 1
cnt = 1

for i in range(1, n):
    if arr[i] > t:
        if (arr[i] > arr[i - 1]):
            cnt += 1
        else:
            max_length = max(max_length, cnt)
            cnt = 1
    else:
        cnt = 1

max_length = max(max_length, cnt)

print(max_length)