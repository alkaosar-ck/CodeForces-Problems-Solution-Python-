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
   #MINGLE_INT = lambda:map(int,input().split())
   
   SINGLE_STR = lambda:input().strip()
   # MINGLE_STR = lambda:map(str,input().split())
   
   #LIST_INT = lambda:list(map(int,input().split()))
   # LIST_INT2 = lambda:list(map(int,input().split()))
   # LIST_STR = lambda:list(map(str,input().split()))
     
   #LIST_SORTED = lambda:sorted(list(map(int,input().split())))
   
   return SINGLE_STR(),SINGLE_STR()


def SUBARRAYS(arr):
    arr = list(str(arr))
    n = len(arr)
    subarrays = []
    for start in range(n):
        for end in range(start, n):
            subarrays.append(arr[start:end + 1])
    return subarrays


def solution():
   n,a = INPUTS()
   s,c,r = 0,{0:1},0
   for i in a:
      s+=int(i)-1  
      if s in c:c[s]+=1
      else:c[s] = 1
      r+=c[s]-1
   print(r)
   
def main():
   test_cases = int(input())
   
   for T in range(test_cases):
       solution()
      
       #print(f'Case{T+1}:{solution()}')
   #solution()

   
   
if __name__ == '__main__':
   main()
