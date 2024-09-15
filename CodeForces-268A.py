u = int(input())
count = 0
test_cases = []
for _ in range(u):
   test_cases.append(list(map(int,input().split())))
for i in range(u):
   for j in range(0,u):
      if test_cases[i][0] == test_cases[j][1]:
         count += 1
print(count)