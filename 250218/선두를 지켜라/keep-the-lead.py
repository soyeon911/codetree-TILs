n, m = map(int, input().split())

a_moves = [tuple(map(int, input().split())) for _ in range(n)]
b_moves = [tuple(map(int, input().split())) for _ in range(m)]

a_pos, b_pos = 0, 0
time_events = []

for speed, duration in a_moves:
    time_events.append((duration, speed, 'a'))

for speed, duration in b_moves:
    time_events.append((duration, speed, 'b'))

time_events.sort()

lead_changes = 0
prev_leader = None

a_idx, b_idx = 0, 0
a_speed, b_speed = 0, 0
a_time, b_time = 0, 0

while a_idx < n or b_idx < n:
    if a_time == 0 and a_idx < n:
        a_speed, a_time = a_moves[a_idx]
        a_idx += 1
    
    if b_time == 0 and b_idx < m:
        b_speed, b_time = b_moves[b_idx]
        b_idx += 1
    
    move_time = min(a_time, b_time)
    a_pos += a_speed * move_time
    b_pos += b_speed * move_time

    a_time -= move_time
    b_time -= move_time

    if a_pos > b_pos:
        curr_leader = 'a'
    elif a_pos < b_pos:
        curr_leader = 'b'
    else:
        curr_leader = prev_leader
    
    if curr_leader != prev_leader and prev_leader is not None:
        lead_changes += 1
    
    prev_leader = curr_leader

print(lead_changes)