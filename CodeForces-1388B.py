import math
for _ in range(int(input())):
   n = int(input())
   eight = math.ceil(n/4)
   nine = n - eight
   answer = ''
   answer+= '9'*nine
   answer+= '8'*eight
   print(answer)
   