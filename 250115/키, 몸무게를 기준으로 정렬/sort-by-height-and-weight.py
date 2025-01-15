n = int(input())

class Chart:
    def __init__(self, name, height, weight):
        self.name = name
        self.height, self.weight = int(height), int(weight)
    
    def __repr__(self):
        return f"{self.name} {self.height} {self.weight}"
    
charts = []

for _ in range(n):
    name, height, weight = input().split()
    charts.append(Chart(name, height, weight))

charts.sort(key = lambda x: (x.height, -x.weight))

for chart in charts:
    print(chart.name, chart.height, chart.weight)