def check(n,s):
   pre = [0]*n
   suf = [0]*n
   prefix = set()
   suffix = set()
   for x in range(n):
      prefix.add(s[x])
      pre[x] = len(prefix)
   for x in range(n-1,-1,-1):
      suffix.add(s[x])
      suf[x] = len(suffix)
   mx = 0
   for i in range(n-1):
      mx = max(mx,pre[i]+suf[i+1])
   return mx
for _ in range(int(input())):
   n = int(input())
   s = input().strip()
   print(check(n,s))