m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoil_list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def f(month, date):
    return sum(num_of_days[:month]) + date

day1 = f(m1, d1)
day2 = f(m2, d2)

elapsed_days = day2 - day1

yoil = 0

result_day = yoil_list[(yoil + elapsed_days) % 7]
print(result_day)