n = int(input())
board = [input().strip() for _ in range(n)]
new = [['0' for _ in range(n)] for _ in range(n)] 
for i in range(n):
    for j in range(n):
        if board[i][j] == '#':
            new[i][j] = '1'
        else:
            new[i][j] = '0'
for i in range(n):
   for j in range(n):
      if new[i][j] == '0':
         try:
            if new[i+1][j-1] == '0' and new[i+1][j]=='0' and new[i+1][j+1] == '0' and new[i+2][j] == '0':
               new[i][j] = '1'
               new[i+1][j-1] = '1'
               new[i+1][j] = '1'
               new[i+1][j+1] = '1'
               new[i+2][j] = '1'
         except:
            pass
possible = True
for x in new:
   if '0' in x:
      possible = False
if possible:
   print('YES')
else:
   print('NO')
         
         