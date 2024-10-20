for _ in range(int(input())):
   s = input().strip()
   t = input().strip()
   if any(s[x] in t for x in range(len(s))):
      print('YES')
      continue
   print('NO')