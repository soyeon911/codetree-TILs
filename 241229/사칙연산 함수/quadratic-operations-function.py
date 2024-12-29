def add(l, m):
    return l + m

def sub(l, m):
    return l - m

def mul(l, m):
    return l * m

def div(l, m):
    if m == 0:
        return "Division by zero"
    return l // m


def caculator(l, n, m):
    if n == "+":
        return add(l, m)
    elif n == "-":
        return sub(l, m)
    elif n == "*":
        return mul(l, m)
    elif n == "/":
        return div(l, m)
    else:
        return False

l, n, m = input().split()
l, m = int(l), int(m)

print(l, n, m, "=",caculator(l, n, m))