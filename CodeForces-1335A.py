t = int(input())
test_case = []
answers = []
for _ in range(t):
   test_case.append(int(input()))
for x in test_case:
   if x == 1 or x == 2:
      answers.append(0)
   elif x == 3:
      answers.append(1)
   else:
      if x%2 == 0:
         result = x//2
         answers.append(result-1)
      else:
         result = (x-1)//2
         answers.append(result)
for case in answers:
   print(case)