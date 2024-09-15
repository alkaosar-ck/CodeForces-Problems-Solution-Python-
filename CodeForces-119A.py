import math

def game(a, b, n):
    turn = 0 
    while n > 0:
        if turn == 0:
            stones = math.gcd(a, n)
        else:
            stones = math.gcd(b, n)
        
        if stones > n:
            return turn
              
        else:
            n -= stones
            turn = 1 - turn 
    return turn
a, b, n = map(int, input().split())
if game(a,b,n) == 1:
   print(0)
else:
   print(1)
