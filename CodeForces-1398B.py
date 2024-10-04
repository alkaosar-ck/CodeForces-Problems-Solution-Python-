for _ in range(int(input())):
   s = input().strip()
   l = []
   l.append(s.split('0'))
   le = []
   for x in l:
      for i in x:
         le.append(len(i))
   le.sort(reverse= True)
   total = 0
   for x in range(0,len(le),2):
      total+=le[x]
   print(total)
      