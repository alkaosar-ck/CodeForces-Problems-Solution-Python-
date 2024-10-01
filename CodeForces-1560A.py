L = [x for x in range(1,2000) if x%3 !=0 and(x%10)!=3]

for _ in range(int(input())):
   i = int(input())
   print(L[i-1])