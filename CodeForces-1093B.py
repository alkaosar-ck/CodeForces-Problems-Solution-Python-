for _ in range(int(input())):
   s = input().strip()
   f = s[0]
   if all(x == f for x in s):
      print(-1)
   else:
      if s != s[::-1]:
         print(s)
      else:
         L = sorted(list(s))
         print(''.join(map(str,L)))
            
      