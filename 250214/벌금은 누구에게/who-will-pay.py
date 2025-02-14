N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]
fines = [0] * (N + 1)

for s in student:
    fines[s] += 1
    
    if fines[s] == K:
        print(s)
        break