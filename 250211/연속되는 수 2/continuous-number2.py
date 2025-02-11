n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

if n == 1:  # 입력이 1개라면, 당연히 1이 정답
    print(1)
    exit()

cnt = 1
result = 1  # 최소한 1개 이상은 존재함

for i in range(1, n):
    if arr[i] == arr[i - 1]:  
        cnt += 1  
    else:  
        result = max(result, cnt)  # 최대값 갱신
        cnt = 1  # 연속 개수 초기화

result = max(result, cnt)  # 마지막 그룹 고려

print(result)
