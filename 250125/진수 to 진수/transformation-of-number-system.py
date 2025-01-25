a, b = map(int, input().split())
n = input()

def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

print(solution(int(n,a),b)) # a진수인 input을 b진수로 바꾸는것