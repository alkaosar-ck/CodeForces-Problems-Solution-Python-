for _ in range(int(input())):
   h,k = map(int,input().split())
   indexs = []
   for i in range(h):
      x = input().strip()
      for j in range(k):
         if x[j] == '#':
            indexs.append((i+1,j+1))
   row = [p[0] for p in indexs]
   col = [p[1] for p in indexs]
   row.sort()
   col.sort()
   r = row[len(row)//2]
   c = col[len(col)//2]
   print(r,c)
   