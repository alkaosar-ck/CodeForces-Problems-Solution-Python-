
s = [2,3]
for _ in range(int(input())):
   i = int(input())
   two_count,tree_count = 0,0
   while i%2 == 0:
      i/=2
      two_count+=1
   while i%3 == 0:
      i/=3
      tree_count +=1
   if i==1 and (tree_count>=two_count):
      print((tree_count-two_count)+tree_count)
   else:
      print(-1)
      