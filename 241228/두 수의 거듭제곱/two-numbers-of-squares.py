import math

def power(n, m):
    return int(math.pow(n, m))

n, m = tuple(map(int, input().split()))
print(power(n, m))