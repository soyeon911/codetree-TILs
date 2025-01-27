n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

OFFSET = 100
MAX_SZ = 200
checked = [0] * (MAX_SZ + 2)

for x1, x2 in segments:
    x1, x2 = x1 + OFFSET, x2 + OFFSET
    for i in range(x1, x2 + 1):
        checked[i] += 1

result = max(checked)
print(result)