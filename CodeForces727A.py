from collections import *
from math import *
from heapq import *
from itertools import *
from queue import *
from cmath import *
from random import *
from functools import *
from time import *
from typing import *
from numbers import *
from fractions import *
from decimal import *
from cmath import *
import sys
import os

def INPUTS():
   #n = int(sys.stdin.readline().strip())
   #arrary = [int(sys.stdin.readline().strip()) for _ in range(n)]
   #SINGLE_INT = lambda:int(input())
   MINGLE_INT = lambda:map(int,input().split())
   
   #SINGLE_STR = lambda:input().strip()
   # MINGLE_STR = lambda:map(str,input().split())
   
   #LIST_INT = lambda:list(map(int,input().split()))
   # LIST_INT2 = lambda:list(map(int,input().split()))
   # LIST_STR = lambda:list(map(str,input().split()))
     
   #LIST_SORTED = lambda:sorted(list(map(int,input().split())))
   
   return MINGLE_INT()




def solution():
   a,b = INPUTS()
   answer = [b]
   while b>a:
      if b%2 == 0:
         answer.append(b//2)
         b//=2
      else:
         s = str(b)
         if (s[-1])!='1':
            print('NO')
            return
         else:
            b = int((s[:-1]))
            answer.append(int(s[:-1]))
   if a == b:
      print("YES")
      print(len(answer))
      print(*answer[::-1])
   else:
      print('NO')
            
      
   
   
   
   
def main():
   # test_cases = int(input())
   
   # for T in range(test_cases):
   #     solution()
      
       #print(f'Case{T+1}:{solution()}')
   solution()

   
   
if __name__ == '__main__':
   main()
