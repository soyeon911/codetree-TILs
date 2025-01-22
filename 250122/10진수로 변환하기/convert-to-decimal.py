binary = list(map(int, list(input())))
n = len(binary)
num = 0

for i in range(n):
    num = num * 2 + binary[i]

print(num)