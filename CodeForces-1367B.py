for _ in range(int(input())):
   i = int(input())
   L = list(map(int,input().split()))
   count = 0
   even_count = sum(1 for x in range(len(L)) if L[x]%2 == 0)
   odd_count  = sum(1 for x in range(len(L)) if L[x]%2 == 1)
   l = len(L)
   if l == 1 and L[0]%2 == 1:
      print(-1)
      continue
   if l%2 == 0 and (even_count == odd_count):
      for x in range(len(L)):
         if x%2 == 0 and L[x]%2 != 0:
            count+=1
         if x%2 == 1 and L[x]%2 == 0:
            count+=1
   elif l%2 == 1 and (odd_count+1==even_count):
      for x in range(len(L)):
         if x%2 == 1 and L[x]%2 == 0:
            count+=1
         if x%2 == 0 and L[x]%2 == 1:
            count+=1
   else:
      print(-1)
      continue
   print(count//2)