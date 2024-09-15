import math
i = list(map(str,input().strip()))
w = i
upper = 0
lower = 0
l = len(i)
for x in range(l):
    if i[x]==i[x].upper():
        upper+=1
    elif i[x]==i[x].lower():
        lower+=1
j = ''.join(i)
if upper>lower:
    print(j.upper())
elif lower>=upper:
    print(j.lower())