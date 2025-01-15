n = int(input())

class Student:
    def __init__(self, number, height, weight):
        self.number = number
        self.height, self.weight = int(height), int(weight)
    
    def __repr__(self):
        return f"{self.height} {self.weight} {self.number}"

students = []

for i in range(1, n + 1):
    height, weight = input().split()
    students.append(Student(i, height, weight))

students.sort(key = lambda x: (-x.height, -x.weight, x.number))

for student in students:
    print(student.height, student.weight, student.number)
