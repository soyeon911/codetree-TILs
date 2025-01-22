binary = input()
binary = list(binary)
n = len(binary)
num = 0

for i in range(n):
    num = num * 2 + int(binary[i])

print(num)