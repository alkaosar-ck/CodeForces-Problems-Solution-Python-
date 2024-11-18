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
   SINGLE_INT = lambda:int(input())
   MINGLE_INT = lambda:map(int,input().split())
   
   SINGLE_STR = lambda:input().strip()
   # MINGLE_STR = lambda:map(str,input().split())
   
   LIST_INT = lambda:list(map(int,input().split()))
   # LIST_INT2 = lambda:list(map(int,input().split()))
   # LIST_STR = lambda:list(map(str,input().split()))
     
   #LIST_SORTED = lambda:sorted(list(map(int,input().split())))
   
   return SINGLE_INT(),SINGLE_STR()




def solution():
   
   n,s = INPUTS()
   t = 0
   x = 0
   while x<n-2:
      if str(s[x:x+3]) == 'map' or str(s[x:x+3]) == 'pie':
         t+=1
         x+=2
      x+=1
   print(t)
   
   
   
def main():
   test_cases = int(input())
   
   for T in range(test_cases):
       solution()
      
       #print(f'Case{T+1}:{solution()}')
   #solution()

   
   
if __name__ == '__main__':
   main()

