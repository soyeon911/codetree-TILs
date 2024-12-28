def leap_year(n):
    if (n % 4 == 0 and n % 100 !=0) or (n % 400 == 0):
        return "true"
    else:
        return "false"

n = int(input())
print(leap_year(n))