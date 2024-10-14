i = int(input())
L = list(map(int, input().split()))
new = []
f = 0

for x in range(i):
   L[x] += f
   f = max(f, L[x])
   new.append(L[x]) 
print(*new)
