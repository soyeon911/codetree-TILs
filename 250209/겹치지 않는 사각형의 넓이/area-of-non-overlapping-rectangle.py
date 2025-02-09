a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = list(map(int, input().split()))

OFFSET = 1000  # 음수 좌표 처리를 위한 보정값
SIZE = 2000  # 격자 크기 (좌표 범위 고려)

box = [[0 for col in range(SIZE + 1)] for row in range(SIZE + 1)]  # 2D 배열 (전체를 0으로 초기화)

def make_box(b):
    x1, y1, x2, y2 = b[0] + OFFSET, b[1] + OFFSET, b[2] + OFFSET, b[3] + OFFSET
    for x in range(x1, x2):
        for y in range(y1, y2):
            box[x][y] = 1

def del_box(m):
    x1, y1, x2, y2 = m[0] + OFFSET, m[1] + OFFSET, m[2] + OFFSET, m[3] + OFFSET
    for x in range(x1, x2):
        for y in range(y1, y2):
            box[x][y] -= 1

make_box(a)
make_box(b)
del_box(m)

result = 0
for x in range(SIZE + 1):
    for y in range(SIZE + 1):
        if box[x][y] == 1:
            result += 1

print(result)