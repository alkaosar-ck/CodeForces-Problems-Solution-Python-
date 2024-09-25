for _ in range(int(input())):
   i = input().strip()
   a = i.count('a')
   b = i.count('b')
   if a == b:
      print('YES')
   else:
      print('NO')