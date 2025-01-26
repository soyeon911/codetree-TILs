n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# 차분 배열 활용
blocks = [0] * (n + 2)

for a, b in commands:
    blocks[a] += 1  # a번째부터 블록 쌓기 시작
    blocks[b + 1] -= 1 # b + 1번째부터는 쌓았던 블록 빼기


# 누적합
curr = 0
max_blocks = 0

for i in range(1, n + 1):
    curr += blocks[i]   # 누적합 계산
    max_blocks = max(max_blocks, curr)  # 최댓값 갱신

print(max_blocks)