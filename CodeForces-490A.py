
i = int(input())
l = list(map(int,input().split()))
if i<3:
   print(0)
   
else:
   programming = l.count(1)
   maths = l.count(2)
   PE = l.count(3)
   mi = min(programming,maths,PE)
   d = {1:0,2:0,3:0}
   for x in l:
      d[x]+=1
   if mi<1:
      print(0)
      
   else:
      print(mi)
      for _ in range(mi):
         f = l.index(1)
         s = l.index(2)
         t = l.index(3)
         print(f+1,s+1,t+1)
         l[f],l[s],l[t] = 0,0,0
         
         
      
   