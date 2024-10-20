for _ in range(int(input())):
   a,b,c,d = map(int,input().split())
   m1 = max(a,b)
   m2 = max(c,d)
   m = max(a,b,c,d)
   l = [a,b,c,d]
   l.remove(m)
   second = max(l)
   if ([m,second] == [a,b] or [second,m] == [a,b]) or ([m,second] == [c,d] or [second,m] == [c,d]):
      print('NO')
   else:
      print('YES')