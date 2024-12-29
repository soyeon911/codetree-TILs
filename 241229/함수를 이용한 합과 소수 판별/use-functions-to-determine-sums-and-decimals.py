def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_even(m):
    if (m % 10 + m // 10) % 2 == 0:
        return True
    return False

def cnt_number(a, b):
    cnt = 0
    for i in range(a, b+1):
        if is_prime(i) and is_even(i):
            cnt += 1
    return cnt


a, b = tuple(map(int, input().split()))
print(cnt_number(a, b))