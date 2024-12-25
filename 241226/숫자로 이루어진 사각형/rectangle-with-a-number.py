
def print_some(n):
    for i in range(n):
        row = [((j % 9) + 1) for j in range(i * n, (i+1)*n)]
        print(" ".join(map(str, row)))

N = int(input())
print_some(N)