o = []
answer = []
t = int(input())
for _ in range(t):
   o.append(int(input()))

for x in o:
   total = 0
   x = str(x)
   for c in x:
      total += int(c)
   answer.append(total)
for case in answer:
   print(case)