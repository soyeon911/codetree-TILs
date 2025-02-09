n = int(input())

OFFSET = 1000
SIZE = 2000

grid = [[0] * SIZE for _ in range(SIZE)]

for _ in range(n):
    a, b = map(int, input().split())

    for i in range(a + OFFSET, a + 8 + OFFSET):
        for j in range(b + OFFSET, b + 8 + OFFSET):
            grid[i][j] = 1

result = sum(row.count(1) for row in grid)
print(result)