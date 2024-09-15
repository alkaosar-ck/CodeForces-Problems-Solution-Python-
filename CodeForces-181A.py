n,m = map(int,input().split())
l = []
row =[]
coloum = []
for _ in range(n):
   l.append(input())
for i in range(n):
   for j in range(m):
      if l[i][j] == '*':
         row.append(i+1)
         coloum.append(j+1)
from collections import Counter
count1 = Counter(row)
count2 = Counter(coloum)
for element,freq in count1.items():
   if freq == 1:
      u_row = element
for element,freq in count2.items():
   if freq == 1:
      u_coloum = element
print(u_row,u_coloum)
   
