a, b, c, d = map(int, input().split())
hour, minu = a, b
result_time = 0

while True:
    if hour == c and minu == d:
        break
    
    result_time += 1
    minu += 1

    if minu == 60:
        hour += 1
        minu = 0

print(result_time)