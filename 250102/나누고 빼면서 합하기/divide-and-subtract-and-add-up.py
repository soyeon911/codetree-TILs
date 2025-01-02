n, m = map(int, input().split())
A = list(map(int, input().split()))

def calculator(n, m, A):
    total = 0
    while m != 1:
        total += A[m - 1]
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    total += A[m - 1]
    return total

result = calculator(n, m, A)
print(result)