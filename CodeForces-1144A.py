for _ in range(int(input())):
   i = input().strip()
   s = set(i)
   if len(s) != len(i):
      print('No')
   else:
      L = sorted(i)
      start = 0
      current = L[start]
      possible = True
      for x in L[1:]:
         if ord(x)-1 != ord(current):
            possible = False
            break
         start+=1
         if L[start]:
            current = L[start]
         else:
            break
      if possible:
         print('Yes')
      else:
         print('No')