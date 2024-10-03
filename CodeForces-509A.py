matrix = [[1]*10 for _ in range(10)]
n = int(input())
for i in range(1,n):
   for j in range(1,n):
      matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]
print(max(max(matrix)))