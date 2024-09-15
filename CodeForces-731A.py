def min_rotation(name: str) -> int:
   total = 0
   current = 'a'
   for char in name:
      clock_wise = abs(ord(char)-ord(current))
      anti_clock = 26-clock_wise
      total+=min(clock_wise,anti_clock)
      current = char
   return total
n = input().strip()
print(min_rotation(n))
