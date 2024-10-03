n,m = map(int,input().split())
inputs = [list(map(int,input().split())) for _ in range(n)]
count = 0
for x in inputs:
   l = len(x)
   for i in range(0,l-1,2):
      if x[i]+x[i+1]>0:
         count+=1
print(count)