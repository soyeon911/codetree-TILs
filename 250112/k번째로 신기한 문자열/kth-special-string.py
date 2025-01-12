n, k, t = input().split()
n, k = int(n), int(k)
words = [input() for _ in range(n)]

# startwith(), endwith() 함수의 이용

def find(n, k, t, words):
    new_list = []
    for word in words:
        if word.startswith(t):
            new_list.append(word)
    new_list.sort()

    if k <= len(new_list):
        return new_list[k-1]
    else:
        return False

result = find(n, k, t, words)
print(result)