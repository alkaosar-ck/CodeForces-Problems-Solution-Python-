answer = []
for _ in range(int(input())):
   n = input()
   n = n.upper()
   if n == 'YES':
      answer.append('YES')
   else:
      answer.append('NO')
for case in answer:
   print(case)