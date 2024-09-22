for _ in range(int(input())):
   i = input()
   if len(i) == 2:
      print(i)
      continue
   else:
      s = ''
      for x in range(len(i)):
         if x%2 == 0:
            s+=i[x]
      s = s+i[-1]
      print(s)