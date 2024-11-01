n,m,k = map(int,input().split())
l = list(map(int,input().split()))
fmx = max(l)
l.remove(fmx)
import math
smx = max(l)
pack = (k*fmx+smx)
total = 0
if k == 1:
   print(fmx*(math.ceil(m/2))+smx*(m//2))
elif k >= m:
   print(fmx*k)
elif m>k:
   times = m//(k+1)
   total+=times*pack
   remain = m%(k+1)
   total+=(remain*fmx)
   print(total)
   