N = int(input())

def print_star(N, curr):
    if curr == 0:
        return

    print("* " * curr)
    print_star(N, curr - 1)
    print("* " * curr)
    

print_star(N, N)