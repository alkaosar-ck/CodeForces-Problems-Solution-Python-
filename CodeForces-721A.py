n = int(input())
a = input().strip()
blocks = []
current_block = a[0]  
for i in range(1, len(a)):
    if a[i] == current_block[0]:
        current_block += a[i] 
    else:
        blocks.append(current_block)  
        current_block = a[i]  
blocks.append(current_block)

n = 0
l = []
for block in blocks:
   if block[0] == 'B':
      n+=1
      l.append(len(block))
print(n)
print(*l)