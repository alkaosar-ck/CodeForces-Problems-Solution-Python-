n = int(input())
l = list(map(int,input().split()))
people = n//2

total_sum = sum(l)

each = round(total_sum/people)

f = l[0]
x = sum(1 for x in l if x == f)

if x == n:
   for i in range(1,n+1,2):
      print(i,i+1)
      
else:
   paired = [False]*n
   for i in range(n):
      if paired[i]:
         continue
      for j in range(i+1,n):
         if not paired[j] and l[i] + l[j] == each:
            print(i+1,j+1)
            paired[i] = paired[j] = True
            break