n,m = map(int,input().split())

while m>=(n*(n+1))//2:
   m = m%(n*(n+1)//2)
for i in range(1,n+1):
   if m<i:
      print(m)
      break
   m-=i