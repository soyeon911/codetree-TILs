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
    if M >= 1 and M <= 12:
        if M in [4, 6, 9, 11]:
            if D in range(1, 31):
                return True
            else:
                return False
        if M == 2:
            if leap_year(Y) == True:
                return True
            else:
                if D in range(1, 29):
                    return True
                return False
        if M in [1, 3, 5, 7, 8, 10, 12]:
            if D in range(1, 32):
                return True
            else:
                return False
    else:
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