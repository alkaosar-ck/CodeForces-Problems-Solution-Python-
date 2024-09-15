def is_prime(n):
   is_prime = True
   r = round(n**0.5)
   if n == 1:
      return False
   else:
      for x in range(2,r+1):
         if n%x == 0:
            is_prime = False
            break
      return is_prime
n = int(input())
for x in range(1,150):
   if is_prime(n*x + 1) == False:
      print(x)
      break