for _ in range(int(input())):
   i = int(input())
   l = sorted(list(map(int,input().split())))
   additional = []
   seen = set()
   for x in l:
      if x in seen:
         additional.append(x)
      else:
         seen.add(x)
   seen = sorted(list(seen))
   p = (seen+additional)
   print(*p)