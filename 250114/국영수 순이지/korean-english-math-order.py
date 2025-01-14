n = int(input())

class Grade:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor, self.eng, self.mat = int(kor), int(eng), int(mat)

grades = []

for _ in range(n):
    name, kor, eng, mat = input().split()
    grades.append(Grade(name, kor, eng, mat))

grades.sort(key = lambda x: (-x.kor, -x.eng, -x.mat))

for grade in grades:
    print(grade.name, grade.kor, grade.eng, grade.mat)

