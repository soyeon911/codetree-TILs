n = int(input())

OFFSET = 1000  # 음수 좌표 처리를 위한 보정값
SIZE = 2000  # 격자 크기 (좌표 범위 고려)

grid = [[0] * SIZE for _ in range(SIZE)]  # 2D 배열 (전체를 0으로 초기화)

for _ in range(n):
    a, b = map(int, input().split())

    # 좌표를 OFFSET을 적용하여 2D 배열에 매핑
    for i in range(a + OFFSET, a + 8 + OFFSET):
        for j in range(b + OFFSET, b + 8 + OFFSET):
            grid[i][j] = 1  # 색칠

# 색칠된 부분(1의 개수) 세기
total_area = sum(row.count(1) for row in grid)

print(total_area)