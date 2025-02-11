n = int(input())
arr = []
cnt = 0
result = 0

for _ in range(n):
    num = int(input())
    arr.append(num)

for i in range(1, n):
    if arr[i] == arr[i - 1]:
        cnt += 1

    else:
        result = max(cnt, result)
        cnt = 1

    result = max(cnt, result)

print(result)