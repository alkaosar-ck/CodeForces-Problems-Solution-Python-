for _ in range(int(input())):
   i = int(input())
   s = input().strip()
   from collections import Counter
   c = Counter(s)
   total = 0
   for x in c:
      if c[x]>1:
         total+=(c[x]+1)
      elif c[x] == 1:
         total+=2
   print(total)