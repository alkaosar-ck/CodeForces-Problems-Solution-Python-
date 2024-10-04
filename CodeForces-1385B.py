for _ in range(int(input())):
   i = int(input())
   L = list(map(int,input().split()))
   main = []
   for x in L:
      if x not in main:    main.append(x)
   print(*main)