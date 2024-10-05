for _ in range(int(input())):
   s = input().strip()
   one = s.count('1')
   zero = s.count('0')
   m = min(one,zero)
   if m%2 == 1:
      print('DA')
   else:
      print('NET')