N = int(input())
string = list(map(int, input().split()))

def abs_val(A):
    for i in range(len(A)):
        A[i] = abs(A[i])

abs_val(string)
print(*string)