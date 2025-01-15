n = 5

class Chart:
    def __init__(self, name, height, weight):
        self.name = name
        self.height, self.weight = int(height), float(weight)
    
    def __repr__(self):
        return f"{self.name} {self.height} {self.weight}"

charts = []

for _ in range(n):
    name, height, weight = input().split()
    charts.append(Chart(name, height, weight))

charts.sort(key = lambda x: x.name)
print("name")
for chart in charts:
    print(chart.name, chart.height, chart.weight)

charts.sort(key= lambda y: -y.height)
print("\nheight")
for chart in charts:
    print(chart.name, chart.height, chart.weight)