for _ in range(int(input())):
   s = input().strip()
   if all(x==s[0] for x in s):
      print('NO')
   else:
      print('YES')
      c = list(s)
      f = c[-1]
      c.pop()
      new = f+''.join(c)
      print(new)