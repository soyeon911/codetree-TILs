M, D = tuple(map(int, input().split()))

def exist(M, D):
    if M >= 1 and M <=12:
        if M == 4 or M == 6 or M == 9 or M == 11:
            if D >= 1 and D <= 30 :
                return True
            else:
                return False
        elif M == 2:
            if D >= 1 and D <= 28:
                return True
            else:
                return False
        else:
            if D >= 1 and D <= 31:
                return True
            else:
                return False
    else:
        return False

if exist(M, D):
    print("Yes")
else:
    print("No")