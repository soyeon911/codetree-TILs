from math import gcd

n = int(input())
arr = list(map(int, input().split()))


def lcm(a, b):
    return (a * b) // gcd(a, b)

def find_lcm(arr, index = 0):
    if index == len(arr) - 1:
        return arr[index]
    return lcm(arr[index], find_lcm(arr, index + 1))

result = find_lcm(arr)
print(result)