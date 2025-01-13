MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

min_index = scores.index(min(scores))

class ent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

union = ent(codenames[min_index], scores[min_index])
print(union.codename, union.score)
