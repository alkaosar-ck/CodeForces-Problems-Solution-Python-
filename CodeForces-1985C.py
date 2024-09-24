def is_good(n,l):
   p_sum = 0
   max_e = 0
   count = 0
   for i in range(n):
      p_sum += l[i]
      max_e = max(max_e,l[i])
      if p_sum-2*max_e==0:
         count+=1
   return count

for _ in range(int(input())):
   n = int(input())
   l = list(map(int,input().split()))
   print(is_good(n,l))