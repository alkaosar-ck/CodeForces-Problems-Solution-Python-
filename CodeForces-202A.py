n = input()
largest_ascii= n[0]
for x in range(1,len(n)):
   if n[x]>largest_ascii :
      largest_ascii = n[x]
c = n.count(largest_ascii)
print(largest_ascii*c)