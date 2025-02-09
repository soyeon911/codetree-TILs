n = int(input())
rect = [tuple(map(int, input().split())) for _ in range(n)] # 0: none, 1: red, 2: blue

OFFSET = 1000
SIZE = 2000

grid = [[0] * (SIZE+1) for _ in range(SIZE + 1)]

def colored_rect(rect):
    for i, (x1, y1, x2, y2) in enumerate(rect):
        color = 1 if i % 2 == 0 else 2  # 짝수 index: red(1), 홀수 index: blue(2)
        for x in range(x1 + OFFSET, x2 + OFFSET):
            for y in range(y1 + OFFSET, y2 + OFFSET):
                grid[x][y] = color

    blue_area = sum(1 for x in range(SIZE + 1) for y in range(SIZE + 1) if grid[x][y] == 2)
    return blue_area

print(colored_rect(rect))