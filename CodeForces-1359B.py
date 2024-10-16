for _ in range(int(input())):
   n,m,x,y = map(int,input().split())
   floor = ['.'*m for _ in range(n)]
   single = 0
   double = 0
   for i in range(n):
      floor[i] = input().strip()
      single+= floor[i].count('.')
   for i in range(n):
      r = floor[i]
      l = list(r)
      for k in range(len(l)-1):
         if l[k] == '.' and l[k+1] == '.':
            double+=1
            l[k] = '*'
            l[k+1] = '*'
            
   remain = single - double*2
   print(min((double*y)+remain*x,single*x))