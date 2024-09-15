n,k = map(int,input().split())
total_time = 60*4
contest_time = total_time-k
count = 0
time_spent = 0
problem_time = 5
for i in range(1,n+1):
   time_need = 5*i
   if time_spent+time_need<=contest_time:
      time_spent+=time_need
      count+=1
   else:
      break
print(count)