def caculator(n, m):
    if n < m:
        m += 25
        n = n * 2
    if n > m:
        n += 25
        m = m * 2
    return n, m

a, b = map(int, input().split())
result = caculator(a, b)
print(*result)