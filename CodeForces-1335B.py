for _ in range(int(input())):
   n,a,b = map(int,input().split())
   f = ord('a')
   if a == 1 or b == 1:
      print(chr(f)*n)
      continue
   uniqe = ''
   l = n
   for x in range(b):
      uniqe+=chr(f+x)
   times = l//b
   uniqe = uniqe*times
   remain = l-(times*b)
   for x in range(remain):
      uniqe+=chr(f+x)
   print(uniqe)