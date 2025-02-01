n = int(input())

OFFSET = 10000
MAX_POS = 20000
tiles = [""] * (MAX_POS + 1)

pos = OFFSET  # 시작 위치

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == "L":
        for i in range(pos, pos - x, -1):  # 현재 위치 포함 x칸 왼쪽 뒤집기
            tiles[i] = "W"
        pos -= x - 1  # 마지막으로 뒤집은 위치로 이동

    elif d == "R":
        for i in range(pos, pos + x):  # 현재 위치 포함 x칸 오른쪽 뒤집기
            tiles[i] = "B"
        pos += x - 1  # 마지막으로 뒤집은 위치로 이동

cnt_w = tiles.count("W")
cnt_b = tiles.count("B")

print(f"{cnt_w} {cnt_b}")
