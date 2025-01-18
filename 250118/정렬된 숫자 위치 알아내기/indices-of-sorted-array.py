n = int(input())
sequence = list(map(int, input().split()))

new_sequence = []
for index, value in enumerate(sequence):
    new_sequence.append((value, index))

# 값 기준으로 정렬
new_sequence.sort(key = lambda x: x[0])

# 결과 저장할 배열
result = [0] * n

for new_index, (value, origin_index) in enumerate(new_sequence):
    result[origin_index] = new_index + 1

print(*result)