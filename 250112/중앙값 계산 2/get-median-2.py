n = int(input())
arr = list(map(int, input().split()))

# def medium_val(n, arr):
#     result = []
#     temp = []

#     for i in range(n):
#         temp.append(arr[i])
#         temp.sort()
#         if (i+1) % 2 != 0:
#             result.append(temp[len(temp) // 2])
#     return result        

# result = medium_val(n, arr)
# print(*result)

# 홀수 번째 수를 지날 때마다 정렬을 진행한 후 가운데 값을 출력함
for i in range(n):
    # 홀수 번째 수는 배열 index가 짝수 !!!!
    if i % 2 == 0:
        sorted_arr = sorted(arr[:i + 1])
        print(sorted_arr[i // 2], end = " ")