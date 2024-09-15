n,k = map(int,input().split())
l = list(map(int,input().split()))
pass_mark = l[k-1]
if pass_mark == 0:
   passed = sum(1 for x in l if x>pass_mark)
else:
   passed = sum(1 for x in l if x>=pass_mark)
print(passed)
