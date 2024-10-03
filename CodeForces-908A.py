s = input().strip()
vowels = ['a','e','i','o','u']
count = 0
if all(x in vowels for x in s):
   print(len(s))
elif all( x not in vowels and not x.isdigit() for x in s):
   print(0)
else:
   for x in s:
      if x.isdigit():
         if int(x)%2 ==1:count+=1
      if x in vowels:count+=1
   print(count)
         
   