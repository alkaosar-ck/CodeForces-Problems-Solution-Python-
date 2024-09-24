n = int(input())
l  = list(map(int,input().split()))
l.sort()
total = 0
s = 0
r = n-1
for x in range(n//2):
   total+= (l[s]+l[r])**2
   s+=1
   r-=1
print(total)