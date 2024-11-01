def generate_subset(number):
   n = len(number)
   subsets = []
   for i in range(1<<n):
      subset = []
      for j in range(n):
         if i & (1<<j):
            subset.append(number[j])
      subsets.append(subset)
   return subsets
def valid(subarray,l,r,x):
   s = sum(subarray)
   m = max(subarray)
   mi = min(subarray)
   diff = m-mi
   if s>=l and s<=r and diff>=x:
      return True
   return False

n,l,r,x = map(int,input().split())
c = list(map(int,input().split()))
possible = sorted(c)
total_ans = 0
total = generate_subset(c)
for k in total:
   if k != []:
      if valid(k,l,r,x):
         total_ans+=1
print(total_ans)