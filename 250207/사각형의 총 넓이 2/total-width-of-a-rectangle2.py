n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)


square1 = (x2[0] - x1[0]) * (y2[0] - y1[0])
square2 = (x2[1] - x1[1]) * (y2[1] - y1[1])

# 겹치는 부분 넓이 계산
overlap_width = max(0, min(x2[0], x2[1]) - max(x1[0], x1[1]))
overlap_height = max(0, min(y2[0], y2[1]) - max(y1[0], y1[1]))
overlap = overlap_width * overlap_height

total = square1 + square2 - overlap
print(total)
