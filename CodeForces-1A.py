
n,m,a = map(int,input().split())
import math
num_flagstones_length = (n + a - 1) // a
num_flagstones_width = (m + a - 1) // a
print(num_flagstones_length*num_flagstones_width)

   
      