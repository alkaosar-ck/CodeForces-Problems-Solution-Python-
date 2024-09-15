for _ in range(int(input())):
   a,b,c = map(int,input().split())
   l = [a,b,c]
   mx = max(l)
   mi = min(l)
   l.remove(mx)
   l.remove(mi)
   middle = l[0]
   if mx-mi == middle:
      print('YES')
   else:
      print('NO')