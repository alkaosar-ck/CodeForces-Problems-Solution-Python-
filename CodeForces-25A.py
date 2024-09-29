i = int(input())
l = list(map(int,input().split()))
even = [x for x in l if x%2 == 0]
odd = [x for x in l if x%2 != 0]
if len(even)>len(odd):
   print(l.index(odd[0])+1)
if len(even)<len(odd):
   print(l.index(even[0])+1)