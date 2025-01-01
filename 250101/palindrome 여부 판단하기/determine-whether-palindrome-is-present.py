def palindrome(A):
    n = len(A)
    for i in range(n // 2):
        if A[i] != A[n-1-i]:
            return False
    return True

_str = input().strip()

if palindrome(_str):
    print("Yes")
else:
    print("No")