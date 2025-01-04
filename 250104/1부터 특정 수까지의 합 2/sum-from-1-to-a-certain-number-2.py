N = int(input())

def Gaussian(N):
    if N == 1:
        return 1
    
    return Gaussian(N - 1) + N

print(Gaussian(N))