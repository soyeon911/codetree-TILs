def gcd(n, m):
    while m != 0:
        n, m = m, n % m
    return n

def lcm(n, m):
    return abs(n*m) // gcd(n, m)

n, m = tuple(map(int, input().split()))
lcm(n, m)
print(lcm(n,m))