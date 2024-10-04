i = input().strip()
len_of_all = len(i)
count_a = i.count('a')
if count_a>(len_of_all//2):
   print(len_of_all)
else:
   while count_a<=(len_of_all//2):
      len_of_all-=1
   print(len_of_all)
