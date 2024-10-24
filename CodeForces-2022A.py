for _ in range(int(input())):
   n,r = map(int,input().split())
   l = list(map(int,input().split()))
   happy = 0
   Rrows = 0
   total = sum(l)
   odds= 0 
   for x in l:
      if x&1 == 0:
         happy+=x
         Rrows+=(x//2)
      else:
         happy+=(x-1)
         R = x//2
         if R == 0:
            Rrows +=1
         else:
            Rrows+=R
         odds+=1
   Rrows = (r-happy//2)
   if Rrows>=odds:
      print(sum(l))
   else:
      print(Rrows*2 - odds+happy)