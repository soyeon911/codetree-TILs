# N은 10진수, q는 진법
n, q = map(int, input().split())

def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)   # divmod() -> 두 값의 몫과 나머지를 tuple로 반환
        rev_base += str(mod)

    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    
print(solution(n, q))
