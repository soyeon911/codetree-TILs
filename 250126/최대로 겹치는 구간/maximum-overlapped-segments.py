n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# 이벤트 리스트 (시작과 끝을 구분)
events = []
for a, b in segments:
    events.append((a, 1))     # 시작점: +1
    events.append((b + 1, -1))  # 끝점 바로 다음: -1 (겹치지 않음)

# 이벤트를 좌표순으로 정렬 (좌표가 같으면 끝점 이벤트가 먼저 처리되도록)
events.sort()

# 현재 겹치는 선분 수와 최대값 계산
current_overlap = 0
max_overlap = 0

for _, event in events:
    current_overlap += event
    max_overlap = max(max_overlap, current_overlap)

print(max_overlap)
