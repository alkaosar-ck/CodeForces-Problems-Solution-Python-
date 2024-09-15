n = int(input())
result= ''
for i in range(1,n+1):
  if i%2 == 0:
    result+='I love '
  else:
    result+='I hate '
  if i!=n:
    result+='that '
result+='it '
print(result)