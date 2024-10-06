for _ in range(int(input())):
   n = int(input())
   if n == 1:print(1);continue
   if n%2 == 1:print(-1);continue
   else:
      for i in range(n):
         if i%2:
            print(i,end=' ')
         else:
            print(n-i,end=' ')