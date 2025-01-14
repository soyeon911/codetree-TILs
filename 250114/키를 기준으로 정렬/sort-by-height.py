n = int(input())

class Scale:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)  # 정렬을 위해 정수형으로 변환
        self.weight = int(weight)  # 정렬을 위해 정수형으로 변환

# Scale 객체를 저장할 리스트
scales = []

# n개의 입력을 받아 객체 생성 및 리스트에 추가
for _ in range(n):
    name, height, weight = input().split()
    scales.append(Scale(name, height, weight))

# 키(height)를 기준으로 정렬
scales.sort(key=lambda x: x.height)

# 정렬된 데이터를 출력
for scale in scales:
    print(scale.name, scale.height, scale.weight)
