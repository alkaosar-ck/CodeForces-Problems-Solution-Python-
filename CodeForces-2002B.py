for _ in range(int(input())):
   i = int(input())
   alice = list(map(int,input().split()))
   bob = list(map(int,input().split()))
   r = alice[::-1]
   if bob == alice or bob == r:
      print('Bob')
   else:
      print('Alice')