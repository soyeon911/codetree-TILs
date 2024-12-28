def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def add_sum(a, b):
    total = 0
    for num in range(a, b+1):
        if is_prime(num):
            total += num
    return total

a, b = tuple(map(int, input().split()))
print(add_sum(a, b))