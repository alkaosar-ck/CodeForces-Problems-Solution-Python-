import math
k = []
t= int(input())
for _ in range(t):
    a = list(input())
    if len(a)>10:
        f = a[0]
        l = a[-1]
        length = len(a)-2
        result = f+str(length)+l
        k.append(result)
    else:
        k.append(a)
 
 
 
for case in k:
    print("".join(case))