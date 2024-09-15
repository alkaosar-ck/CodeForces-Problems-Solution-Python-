m_w = 0
c_w = 0
for _ in range(int(input())):
   m,c = map(int,input().split())
   if m>c:
      m_w+=1
   elif c>m:
      c_w += 1
if m_w>c_w:
   print('Mishka')
elif m_w == c_w:
   print("Friendship is magic!^^")
else:
   print('Chris')