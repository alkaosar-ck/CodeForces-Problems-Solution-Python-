for _ in range(int(input())):
   a = input()
   l = a.split('+')
   count = 0
   for x in l:
      count += int(x)
   print(count)