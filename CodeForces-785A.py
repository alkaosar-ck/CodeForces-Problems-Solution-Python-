l = []
for _ in range(int(input())):
   l.append(input().strip())

total = 0
for x in l:
   if x == 'Dodecahedron':
      total+=12
   elif x == 'Cube':
      total+=6
   elif x == 'Tetrahedron':
      total += 4
   elif x == 'Octahedron':
      total+=8
   elif x == 'Icosahedron':
      total+=20
print(total)