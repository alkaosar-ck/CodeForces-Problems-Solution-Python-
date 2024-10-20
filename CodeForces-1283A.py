for _ in range(int(input())):
   h,m = map(int,input().split())
   remain_hour = 23-h
   remain_minute = 60-m
   total = remain_hour*60 + remain_minute
   print(total)