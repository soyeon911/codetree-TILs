N = int(input())

def fac(n):
    if n == 0:
        return 1

    if n == 1:
        return 1
    
    return fac(n - 1) * (n % 10)

result = fac(N)
print(result)