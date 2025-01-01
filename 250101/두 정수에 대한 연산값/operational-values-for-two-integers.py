def caculator(n, m):
    if n < m:
        m += 25
        n = n * 2
    elif n > m:
        n += 25
        m = m * 2
    return n, m

a, b = map(int, input().split())
caculator(a, b)
print(*caculator(a, b))