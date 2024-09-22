for _ in range(int(input())):
   i = int(input())
   if 1900 <=i:
      print('Division 1')
   elif 1600 <=i and i<=1899:
      print('Division 2')
   elif i>=1400 and i<=1599:
      print('Division 3')
   else:
      print('Division 4')