n = int(input())
l = list(map(int,input().split()))
current_highest = l[0]
current_lowest = l[0]
count = 0
if n == 1:
   print(0)
else:
   for x in l:
      if x>current_highest:
         count+=1
         current_highest = x
      elif x<current_lowest:
         count+=1
         current_lowest = x
   print(count)