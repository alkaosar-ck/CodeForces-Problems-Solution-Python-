for _ in range(int(input())):
   i = sorted(list(map(int,input().split())))
   for x in range(5):
      i[0]+=1
      i.sort()
   print(i[0]*i[1]*i[2])
      