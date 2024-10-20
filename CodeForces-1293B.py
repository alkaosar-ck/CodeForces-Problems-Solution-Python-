i = int(input())
answer = 0
for x in range(1,i+1):
   answer += (1/x)
print(f'{answer:.12f}')