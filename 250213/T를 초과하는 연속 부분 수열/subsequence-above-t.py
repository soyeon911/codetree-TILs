n, t = map(int, input().split())  # N: 수열 길이, T: 기준 숫자
arr = list(map(int, input().split()))  # 수열 입력

max_length = 0  # 최장 연속 부분 수열 길이
cnt = 0  # 현재 연속 부분 수열의 길이

for i in range(n):
    if arr[i] > t:  
        cnt += 1  # T보다 크면 연속 부분 수열 길이 증가
    else:
        max_length = max(max_length, cnt)  # 최대 길이 갱신
        cnt = 0  # 연속 부분 수열 초기화

# 마지막 연속 부분 수열 고려
max_length = max(max_length, cnt)

print(max_length)
