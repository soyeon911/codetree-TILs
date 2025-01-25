N = list(map(int, list(input())))
n = len(N)
num = 0

# 10진수 변환
for i in range(n):
    num = num * 2 + N[i]

# 17배
num *= 17
results = []

# 다시 이진수로 변환
while True:
    if num < 2:
        results.append(num)
        break
    
    results.append(num % 2)
    num //= 2

for result in results[::-1]:
    print(result, end = "")