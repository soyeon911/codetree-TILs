def gcd(n, m):
    while m != 0:
        n, m = m,  n % m
    return n

n, m = tuple(map(int, input().split()))
gcd(n, m)
print(gcd(n,m))