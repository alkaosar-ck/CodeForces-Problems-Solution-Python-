n = int(input())
matrix = []
for i in range(n):
      l =(list(map(int,input().split())))
      matrix.append(l)
main_dia = sum(matrix[i][i] for i in range(n))
side_dia= sum(matrix[i][n-i-1] for i in range(n) if i!= n-1-i)
sum_of_dia = main_dia+side_dia
total = sum_of_dia
if n%2 == 1:
   import math
   m = math.floor(n/2)
   middle_row = sum(matrix[m][i] for i in range(n) if i!=m)
   middle_co = sum(matrix[i][m] for i in range(n) if i!=m)
   sum_of_row_coloum = middle_co+middle_row
   total = sum_of_dia+sum_of_row_coloum
print(total)