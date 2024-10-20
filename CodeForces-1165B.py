i = int(input())
l = list(map(int, input().split()))
l.sort() 
start = 1
total = 0

for x in l:
    if x >= start:
        total += 1  
        start += 1  
       
print(total)
