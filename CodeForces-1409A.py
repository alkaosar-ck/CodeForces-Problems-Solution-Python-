answer = []
for _ in range(int(input())):
   a,b = map(int,input().split())
   find = abs(a-b)
   count = 0
   if a == b:
      answer.append(0)
      continue
   else:
        moves = (find + 9) // 10 
        answer.append(moves)
      
for case in answer:
   print(case)
      