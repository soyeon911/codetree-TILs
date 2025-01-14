n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

class WeatherCast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

# 각 날짜별로 객체 생성
weather_objects = [WeatherCast(date[i], day[i], weather[i]) for i in range(n)]

# 비가 오는 날만 필터링
rainy_days = [obj for obj in weather_objects if obj.weather == "Rain"]

# 결과 출력
if rainy_days:
    # 날짜 기준으로 정렬 후 가장 빠른 날의 정보 출력
    earliest_rainy_day = sorted(rainy_days, key=lambda x: x.date)[0]
    print(f"{earliest_rainy_day.date} {earliest_rainy_day.day} {earliest_rainy_day.weather}")
else:
    print("No rainy days found.")