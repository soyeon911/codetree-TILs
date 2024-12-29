def is_onjeonsu(n):
    if n % 2 != 0 and n % 10 != 5 and not(n % 3 == 0 and n % 9 != 0):
        return True
    return False

def cnt_number(a, b):
    cnt = 0
    for i in range(a, b+1):
        if is_onjeonsu(i):
            cnt += 1
    return cnt

a, b = tuple(map(int, input().split()))
print(cnt_number(a, b))