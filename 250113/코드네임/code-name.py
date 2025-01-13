MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

class ent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

scores.sort()
union = ent(codenames[0], scores[0])
print(union.codename, union.score)
