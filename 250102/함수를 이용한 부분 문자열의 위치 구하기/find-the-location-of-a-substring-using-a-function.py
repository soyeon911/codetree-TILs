input_str = input().strip()
traget_str = input().strip()

def find_index(input_str, traget_str):
    index = input_str.find(traget_str)
    return index

result = find_index(input_str, traget_str)

if result != -1:
    print(result)
else:
    print("-1")