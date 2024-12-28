def leap_year(n):
    if n % 4 == 0:
        return "true"
    
    if n % 100 == 0 and n % 400 != 0:
        return "false"

n = int(input())
print(leap_year(n))