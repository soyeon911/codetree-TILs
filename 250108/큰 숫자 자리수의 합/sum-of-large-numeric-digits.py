a, b, c = map(int, input().split())

def f(a, b, c):
    return a * b * c

def g(N):
    if N == 0:
        return 0
    return g(N // 10) + (N % 10)

result = f(a, b, c)
summation = g(result)
print(summation)
