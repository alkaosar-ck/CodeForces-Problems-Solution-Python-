
for _ in range(int(input())):
   sub = []
   i = int(input())
   L = list(map(int,input().split()))
   L.sort()
   for x in range(1,i):
      sub.append(abs(L[x]-L[x-1]))
   print(min(sub))