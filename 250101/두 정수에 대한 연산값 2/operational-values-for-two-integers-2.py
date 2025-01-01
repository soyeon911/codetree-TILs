def caculator(a, b):
    if a > b:
        b += 10
        a = a * 2
    elif a < b:
        a += 10
        b = b * 2
    return a, b

a, b = map(int, input().split())
caculator(a, b)
print(*caculator(a, b))