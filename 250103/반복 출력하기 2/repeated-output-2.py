n = int(input())

def print_str(n):
    if n == 0:
        return
    
    print_str(n - 1)
    print("HelloWorld")

print_str(n)