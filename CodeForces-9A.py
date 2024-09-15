a, b = map(int, input().split())
m = max(a, b)
numerator = 7 - m 
denominator = 6
import math
gcd_value = math.gcd(numerator, denominator)
numerator //= gcd_value
denominator //= gcd_value
if a == 1 and b == 1:
   print('1/1')
else:
    print(f"{numerator}/{denominator}")
