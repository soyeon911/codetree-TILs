m1, d1, m2, d2 = map(int, input().split())
A = input()

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoil_list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def f(month, date):
    return sum(num_of_days[:month])+ date

start_day = yoil_list.index(A)

day1 = f(m1, d1)
day2 = f(m2, d2)

elapsed_day = day2 - day1

cnt = 0
for i in range(elapsed_day + 1):
    current_day = (start_day + i) % 7
    if yoil_list[current_day] == A:
        cnt += 1

print(cnt)