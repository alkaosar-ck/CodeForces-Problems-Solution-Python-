u = []
for _ in range(int(input())):
   a,b = map(int,input().split())
   u.append(abs(a-b))
for case in u:
   print(case)