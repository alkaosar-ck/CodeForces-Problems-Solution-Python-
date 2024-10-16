for _ in range(int(input())):
   i = int(input())
   L = sorted(list(map(int,input().split())))
   print(abs(L[i]-L[i-1]))