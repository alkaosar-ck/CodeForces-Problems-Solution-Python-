for _ in range(int(input())):
   n = input()
   count = 1
   for x in range(1,len(n)):
      if n[x] != '0':
         count+=1
   print(count)
   u = []
   p = 0
   for x in range(len(n)-1,-1,-1):
      a = int(n[x])
      if a == 0:
         p+=1
         continue
         
      else:
         u.append(a*(10**p))
      p+=1
   print(*u)
         