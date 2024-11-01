def get(x):
   return x*(x+1)//2
def solution():
   #n, k = map(int, input().split())
   t = int(input())
   #L = list(map(int, input().split()))
   #H = list(map(int,input().split()))
   total = 0
   start = 1
   while get((1<<start)-1)<=t:
      t-=get((1<<start)-1)
      start+=1
      total+=1
   print(total)
def main():
   for _ in range(int(input())):
      solution()
# solution()
if __name__ == '__main__':
   main()
