a = list(input().strip())
b = list(input().strip())
total = 0
l1,l2 = len(a),len(b)
m = min(l1,l2)
for x in range(-1,-m-1,-1):
   try: 
      if a[x] == b[x]:
         total += 1
      else:
         break
   except:
      break
a = a[:l1-total]
b = b[:l2-total]
print(len(a)+len(b))
   