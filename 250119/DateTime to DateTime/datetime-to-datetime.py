a, b, c = map(int, input().split())
day, hour, minu = 11, 11, 11


if a < day or (a == day and b < hour) or (a == day and b == hour and c < minu):
    print("-1")
    
else:
    result_mins = (a - day) * 24 * 60 + (b - hour) * 60 + (c - day)
    print(result_mins)