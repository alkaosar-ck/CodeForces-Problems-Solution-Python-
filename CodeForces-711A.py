t = int(input())
seats = [input().strip() for _ in range(t)]
is_true = False
numbers = []
for i in range(t):
   seat = list(seats[i])
   if seat[0] == 'O' and seat[1] == 'O':
      is_true = True
      seat[0] = '+'
      seat[1] = '+'
      seats[i] = ''.join(seat)
      break
   if seat[3] == 'O' and seat[4] == 'O':
      is_true = True
      seat[3] = '+'
      seat[4] = '+'
      seats[i] = ''.join(seat)
      break
if is_true:
   print('YES')
   for seat in seats:
      print(seat)
else:
   print('NO')
