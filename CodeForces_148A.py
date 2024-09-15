k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

main = [i for i in range(1,d+1)]
l_for_l = [i for i in range(l,d+1) if i%l == 0]
l_for_m = [i for i in range(m,d+1) if i%m == 0]
l_for_n = [i for i in range(n,d+1) if i%n == 0]
l_for_k = [i for i in range(k,d+1) if i%k == 0]

sub = set(l_for_k)|set(l_for_l)|set(l_for_m)|set(l_for_n)

total = set(main).symmetric_difference(set(sub))

if total:
   print(d-len(total))
else:
   print(d)