for _ in range(int(input())):
   i = int(input())
   s = input().strip()
   answer = ''
   for x in range(0,len(s),2):
      answer+=s[x]
   print(answer)