n,k = list(map(int,input().split()))
l = list(map(int,input().split()))
n =sorted(l)
count= 0
for x in range(0,len(n),3):
   try:
      if k+n[x]<=5 and k+n[x+1]<=5 and k+n[x+2]<=5:
         count+=1
   except:
      break
print(count)