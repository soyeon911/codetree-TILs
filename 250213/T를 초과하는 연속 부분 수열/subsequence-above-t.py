n, t = map(int, input().split())  
arr = list(map(int, input().split()))  

max_length = 0 
cnt = 0

for i in range(n):
    if arr[i] > t:  
        cnt += 1 
    else:
        max_length = max(max_length, cnt)  
        cnt = 0  


max_length = max(max_length, cnt)

print(max_length)
