A = []

def range_sum(a1, a2):
    return sum(A[a1 - 1:a2])  


n, m = map(int, input().split())
A = list(map(int, input().split()))

results = []


for _ in range(m):
    a1, a2 = map(int, input().split())
    results.append(range_sum(a1, a2))


for result in results:
    print(result)
