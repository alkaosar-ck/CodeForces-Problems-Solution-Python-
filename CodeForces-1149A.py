b = int(input())
H = list(map(int,input().split()))
cnt2,cnt1 = H.count(2),H.count(1)
if b == 1:
   print(*H)
elif b == 2:
   H.sort(reverse=True)
   print(*H)
elif cnt2>0 and cnt1>0:
   answer = [2,1]
   cnt1-=1
   cnt2-=1
   while cnt2:
      answer.append(2)
      cnt2-=1
   while cnt1:
      answer.append(1)
      cnt1-=1
   print(*answer)
else:
   print(*sorted(H))
      
   