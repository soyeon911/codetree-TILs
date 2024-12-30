Y, M, D = tuple(map(int, input().split()))

def leap_year(Y):
    if Y % 4 != 0:
        return False
    if Y % 100 != 0:
        return True
    if Y % 400 == 0:
        return True
    return False

def exist_day(Y, M, D):
    days_in_month = [31, 29 if leap_year(Y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    
    if 1 <= M <= 12:
        return 1 <= D <= days_in_month[M - 1]
    return False


def season(M):
    if M in [3, 4, 5]:
        print("Spring")
    if M in [6, 7, 8]:
        print("Summer")
    if M in [9, 10, 11]:
        print("Fall")
    if M in [12, 1, 2]:
        print("Winter")

if exist_day(Y, M, D) == False:
    print("-1")
else:
    season(M)