for _ in range(int(input())):
   i = input().strip()
   if len(i) % 2 == 1:
      print('NO')
   else:
      m = len(i)//2
      if i[:m] == i[m:]:
         print('YES')
      else:
         print('NO')
  
