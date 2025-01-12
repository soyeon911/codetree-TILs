word1 = input().strip()
word2 = input().strip()

def f(word1, word2):
    return sorted(word1) == sorted(word2)

f(word1, word2)
if f(word1, word2):
    print("Yes")
else:
    print("No")
