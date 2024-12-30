n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def continuous(A, B):
    n1, n2 = len(A), len(B)
    for i in range(n1 - n2 + 1):
        if A[i : i + n2] == B:
            return True
    return False


if continuous(A, B):
    print("Yes")
else:
    print("No")