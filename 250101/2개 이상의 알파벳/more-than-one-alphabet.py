def check_distinct_alpha(s):
    A = set(s)

    if len(A) >= 2:
        return True
    else:
        return False

N = input().strip()
check_distinct_alpha(N)

if check_distinct_alpha(N):
    print("Yes")
else:
    print("No")