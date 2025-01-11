n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def f(A, B):
    for a in A:
        if a not in B:
            return False
    return True

f(A, B)
if f(A, B):
    print("Yes")
else:
    print("No")