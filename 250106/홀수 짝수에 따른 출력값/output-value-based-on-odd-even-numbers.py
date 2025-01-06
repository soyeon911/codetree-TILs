N = int(input())

def f(n, curr = 1, sumation = 0):
    if curr > n:
        return sumation

    if n % 2 == 0 and curr % 2 == 0:
        sumation += curr

    elif n % 2 != 0 and curr % 2 != 0:
        sumation += curr
    
    return f(n, curr + 1, sumation)
    
result = f(N)
print(result)