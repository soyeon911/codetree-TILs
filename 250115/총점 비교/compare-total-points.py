n = int(input())

class Grade:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1, self.score2, self.score3 = int(score1), int(score2), int(score3)

scores = []

for _ in range(n):
    name, score1, score2, score3 = input().split()
    scores.append(Grade(name, score1, score2, score3))


scores.sort(key=lambda x: (x.score1 + x.score2 + x.score3))

for score in scores:
    print(score.name, score.score1, score.score2, score.score3)