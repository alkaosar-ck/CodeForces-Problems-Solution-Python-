i = int(input())
l = list(map(int,input().split()))
must = l.count(4)
single = l.count(1)
double = l.count(2)
one_missing = l.count(3)
total = must
pairs = min(single,one_missing)
total+=pairs
one_missing-=pairs
single-=pairs

total+=one_missing

total+=double//2
if double&1 == 1:
   total+=1
   single-=min(2,single)
if single>0:
   total+=(single+3)//4

print(total)
      
      