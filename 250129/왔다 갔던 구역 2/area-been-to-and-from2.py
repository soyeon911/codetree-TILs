n = int(input())

OFFSET = 10000
MAX_POS = 20000
visited = [0] * (MAX_POS + 1)

pos = OFFSET

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == "L":
        for i in range(pos - x, pos):
            visited[i] += 1
        pos -= x
    
    elif d == "R":
        for i in range(pos, pos + x):
            visited[i] += 1
        pos += x

cnt = sum(1 for v in visited if v >= 2)
print(cnt)
