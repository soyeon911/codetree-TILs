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
overlap = (x2[0] - x1[1]) * (y2[1] - y1[1])

print(square1 + square2 - overlap)
