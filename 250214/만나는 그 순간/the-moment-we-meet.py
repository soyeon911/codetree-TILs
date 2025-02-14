n, m = tuple(map(int, input().split()))

a_arr = [tuple(input().split()) for _ in range(n)]
b_arr = [tuple(input().split()) for _ in range(m)]

a_ans_arr = []
a_base = 0

for direction, distance in a_arr:
    distance = int(distance)
    if direction == 'R':
        while distance > 0:
            a_base += 1
            distance -= 1
            a_ans_arr.append(a_base)
    else:
        while distance > 0:
            a_base -= 1
            distance -= 1
            a_ans_arr.append(a_base)

b_ans_arr = []
b_base = 0

for direction, distance in b_arr:
    distance = int(distance)
    if direction == 'R':
        while distance > 0:
            b_base += 1
            distance -= 1
            b_ans_arr.append(b_base)
    else:
        while distance > 0:
            b_base -= 1
            distance -= 1
            b_ans_arr.append(b_base)

result = 0

for i in range(max(len(a_ans_arr), len(b_ans_arr))):
    if a_ans_arr[i] == b_ans_arr[i]:
        result = i + 1
        print(result)
        break
    else:
        print(-1)