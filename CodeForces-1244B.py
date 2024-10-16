for _ in range(int(input())):
   i = int(input())
   s = input().strip()
   if s[0] == '1' or s[-1] == '1':
      print(i*2)
   else:  
      if '1' in s:
         index = s.index('1')
         s = s[::-1]
         index2 = s.index('1')
         m = min(index,index2)
         m = i-m
         print(2*m)
      else:
         print(i)
   