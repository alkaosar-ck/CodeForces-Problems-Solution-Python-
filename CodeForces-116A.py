n = int(input()) 
o = []
for _ in range(n):
    a, b = map(int, input().split())
    o.append((a, b))
 
current_passengers = 0  
max_passengers = 0 
for x in range(n):
    a, b = o[x]
    current_passengers -= a  
    current_passengers += b  
    max_passengers = max(max_passengers, current_passengers)  
 
print(max_passengers)