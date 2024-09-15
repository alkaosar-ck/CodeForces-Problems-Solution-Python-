n,m = map(int,input().split())
l = [input().split() for _ in range(n)]
if any(char in ['C','M','Y'] for row in l for char in row):
   print('#Color')
else:
   print('#Black&White')