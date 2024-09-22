for _ in range(int(input())):
   i = input().strip()
   s1 = int(i[0])+int(i[1])+int(i[2])
   s2 = int(i[-1])+int(i[-2])+int(i[-3])
   if s1 == s2:
      print('YES')
   else:
      print('NO')