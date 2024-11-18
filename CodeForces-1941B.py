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
   #MINGLE_INT = lambda:map(int,input().split())
   
   #SINGLE_STR = lambda:input().strip()
   # MINGLE_STR = lambda:map(str,input().split())
   
   LIST_INT = lambda:list(map(int,input().split()))
   # LIST_INT2 = lambda:list(map(int,input().split()))
   # LIST_STR = lambda:list(map(str,input().split()))
     
   #LIST_SORTED = lambda:sorted(list(map(int,input().split())))
   
   return SINGLE_INT(),LIST_INT()


def solution():
   n,l = INPUTS()
   if all(x == 0 for x in l):
      print('YES')
      return
   if all(x == l[0] for x in l) and l[0]!=0:
      print('NO')
      return
   for i in range(n-2):
      if l[i]<0:
         print('NO')
         return
      dp = l[i]
      l[i]-=dp
      l[i+1]-=dp*2
      l[i+2]-=dp
   if l[-1]!=0 or l[-2]!=0:
      print('NO')
   else:
      print('YES')
   
def main():
   test_cases = int(input())
   
   for T in range(test_cases):
       solution()
      
       #print(f'Case{T+1}:{solution()}')
   #solution()

   
   
if __name__ == '__main__':
   main()

