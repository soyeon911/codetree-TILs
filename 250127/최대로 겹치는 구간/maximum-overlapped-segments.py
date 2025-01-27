n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

OFFSET = 100
MAX_SZ = 200

checked = [0] * (MAX_SZ + 1)

for x1, x2 in segments:
    x1, x2 = x1 + OFFSET, x2 + OFFSET
    for i in range(x1, x2):
        checked[i] += 1

result = max(checked)
print(result)

# # 이벤트 방식 사용
# events = []
# for a, b in segments:
#     events.append((a, 1))   # 선분의 시작: +1
#     events.append((b, -1))  # 선분의 끝: -1 (b에서 끝남)

# # 좌표 정렬 (같은 좌표에서는 끝 이벤트가 먼저 처리되도록 설정)
# events.sort(key=lambda x: (x[0], x[1]))

# # 최대 겹침 계산
# current_overlap = 0
# max_overlap = 0

# for _, event in events:
#     current_overlap += event
#     max_overlap = max(max_overlap, current_overlap)

# print(max_overlap)
