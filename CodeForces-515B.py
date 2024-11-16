from math import gcd
n,m=map(int,input().split())
gcdd=gcd(n,m)
l=list(map(int,input().split()));r=[0]*gcdd
for i in l[1:]:
 r[i%gcdd]=1
l1=list(map(int,input().split()))
for j in l1[1:]:
 r[j%gcdd]=1
for i in r:
  if i==0:exit(print("No"))
print("Yes")
