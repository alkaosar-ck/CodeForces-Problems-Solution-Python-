n,k = map(int,input().split())
l = sorted(set(list(map(int,input().split()))))
if l:
   print(l[0])
else:
   print(0)
   exit()
for i in range(1,k):
   if i<len(l):
      s = l[i]-l[i-1]
      print(s if s>0 else 0)
   else:
      print(0)
