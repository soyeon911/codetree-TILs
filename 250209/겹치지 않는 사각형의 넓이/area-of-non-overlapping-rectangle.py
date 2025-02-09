x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

for i in range(3):
    x1[i], y1[i], x2[i], y2[i] = map(int, input().split())

A, B, M = 0, 1, 2

# A, B 의 기존 넓이
area_A = (x2[A] - x1[A]) * (y2[A] - y1[A])
area_B = (x2[B] - x1[B]) * (y2[B] - y1[B])

# M 이 A를 덮는 영역
overlap_A_width = max(0, min(x2[A], x2[M]) - max(x1[A], x1[M]))
overlap_A_height = max(0, min(y2[A], y2[M]) - max(x1[A], x1[M]))
overlap_A = overlap_A_width * overlap_A_height

# M 이 B를 덮는 영역
overlap_B_width = max(0, min(x2[B], x2[M]) - max(x1[B], x1[M]))
overlap_B_height = max(0, min(y2[B], y2[M]) - max(y1[B], y1[M]))
overlap_B = overlap_B_width * overlap_B_height

# 잔여 A, B 넓이 합
result = area_A + area_B - overlap_A - overlap_B
print(result)