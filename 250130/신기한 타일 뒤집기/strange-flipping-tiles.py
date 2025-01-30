n = int(input())

OFFSET = 10000
MAX_POS = 20000
tiles = [""] * (MAX_POS + 1)

pos = OFFSET

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == "L":
        for i in range(pos - x, pos):
            if tiles[i] == "" or tiles[i] == "B":
                tiles[i] = "W"
        pos -= x
    
    elif d == "R":
        for i in range(pos, pos + x):
            if tiles[i] == "" or tiles[i] == "W":
                tiles[i] = "B"
        pos += x

cnt_b = sum(1 for tile in tiles if tile == "B")
cnt_w = sum(1 for tile in tiles if tile == "W")

print(f"{cnt_w} {cnt_b}")