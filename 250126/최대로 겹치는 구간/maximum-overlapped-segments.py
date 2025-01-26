n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

max_point = max(b for _, b in segments)

lines = [0] * (max_point + 2)

for a, b in segments:
    lines[a] += 1
    lines[b + 1] -= 1

curr = 0
max_line = 0

for line in lines:
    curr += line
    max_line = max(max_line, curr)
    
print(max_line)