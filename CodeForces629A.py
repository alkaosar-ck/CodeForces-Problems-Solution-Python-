n = int(input())  
inputs = [input().strip() for _ in range(n)]  
row_pairs = 0
col_pairs = 0
for x in inputs:
    c = x.count('C')  
    row_pairs += c * (c - 1) // 2  
for i in range(n):  
    current = 0 
    for x in range(n): 
        if inputs[x][i] == 'C': 
            current += 1  
    col_pairs += current * (current - 1) // 2 
print(row_pairs + col_pairs)
