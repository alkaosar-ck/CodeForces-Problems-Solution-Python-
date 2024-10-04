k2,k3,k5,k6 = map(int,input().split())
m = min(k2,k5,k6)
total = 256*m
k2-=m
if k2>0:
   m = min(k2,k3)
   total+=(32)*m
print(total)