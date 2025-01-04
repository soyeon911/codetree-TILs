N = int(input())

def print_num(N, curr):
    if curr == 0:
        return

    
    print(curr, end = " ")
    print_num(N, curr - 1)
    print(curr, end = " ")

print_num(N, N)