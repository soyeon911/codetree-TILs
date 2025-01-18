n = int(input())
# students = [
#     (h, w, i + 1)
#     for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
# ]

class Student:
    def __init__(self, height, weight, num):
        self.height, self.weight = int(height), int(weight)
        self.num = num

students = []
for i in range(1, n+1):
    height, weight = input().split()
    students.append(Student(height, weight, i))

students.sort(key=lambda x: (x.height, -x.weight))

for student in students:
    print(student.height, student.weight, student.num)