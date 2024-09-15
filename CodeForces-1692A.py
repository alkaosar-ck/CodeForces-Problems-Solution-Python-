
answer = []
for _ in range(int(input())):
   a,b,c,d = map(int,input().split())
   l = [a,b,c,d]
   s = [b,c,d]
   case = sum(1 for x in s if a<x)
   answer.append(case)
for case in answer:
   print(case)
   