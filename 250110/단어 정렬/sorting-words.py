n = int(input())
word = [input() for _ in range(n)]

def sort(word):
    word.sort()
    return word

sorted_word = sort(word)
print("\n".join(sorted_word))
