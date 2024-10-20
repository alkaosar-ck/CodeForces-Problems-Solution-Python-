i = int(input())
l = list(map(int, input().split()))

l = l[::-1] 
prev = l[0] 
total = 0    
for x in l:
    if prev > 0:
        total += min(prev, x)  
        prev = min(prev - 1, x-1)  
    else:
        break  
print(total)
