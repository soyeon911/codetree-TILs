N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]
fines = [0] * (N + 1)

ans = -1
for s in student:
    fines[s] += 1
    
    if fines[s] == K:
        ans = s
        break
print(ans)