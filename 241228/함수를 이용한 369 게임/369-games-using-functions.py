def cnt_number(n, m):
    cnt = 0
    for i in range(n, m+1):
        if game_number(i):
            cnt += 1

    return cnt

def game_number(l):
    if l % 3 == 0:
        return True
        
    for digit in str(l):  
        if digit in "369":
            return True
            
    else:
        return False

n, m = tuple(map(int, input().split()))
print(cnt_number(n, m))
