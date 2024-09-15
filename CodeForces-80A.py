import math

def sieve_of_eratosthenes(limit):
  
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  
    
    
    for p in range(2, int(math.sqrt(limit)) + 1):
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
    
    return [p for p in range(limit + 1) if primes[p]]

LIMIT = 2000
all_primes = sieve_of_eratosthenes(LIMIT)

n,m = map(int,input().split())
i = all_primes.index(n)
s = all_primes[i+1]
if m == s:
   print('YES')
else:
   print('NO')