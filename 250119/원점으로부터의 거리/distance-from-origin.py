n = int(input())

class Point:
    def __init__(self, x, y, distance, num):
        self.x, self.y, self.distance, self.num = x, y, distance, num
    

points = []
for i in range(1, n+1):
    x, y = tuple(map(int, input().split()))
    distance = abs(x) + abs(y)
    points.append(Point(x, y, distance, i))

points.sort(key = lambda x: (x.distance, x.num))

for point in points:
    print(point.num)
