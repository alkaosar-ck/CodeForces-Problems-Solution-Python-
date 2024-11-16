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
import sys
import os
import decimal

def INPUTS():
   #n = int(sys.stdin.readline().strip())
   #arrary = [int(sys.stdin.readline().strip()) for _ in range(n)]
   
   SINGLE_INT = lambda:int(input())
   #MINGLE_INT = lambda:map(int,input().split())
   
   #SINGLE_STR = lambda:input().strip()
   # MINGLE_STR = lambda:map(str,input().split())
   
   LIST_INT = lambda:list(map(int,input().split()))
   #LIST_INT2 = lambda:list(map(int,input().split()))
   # LIST_STR = lambda:list(map(str,input().split()))
     
   # LIST_SORTED = lambda:sorted(list(map(int,input().split())))
   n = SINGLE_INT()
   l = LIST_INT()
   return n,l
    

def solution():
   n,l=INPUTS()
   l = sorted(l)
   s = set()
   
   if len(set(l))>3:
      print(-1)
      return
   
   if len(set(l)) == 1:
      print(0)
      return
   
   if len(set(l)) == 2:
      if ((max(l)-min(l))/2).is_integer():
         print((max(l)-min(l))//2)
      else:
         print(max(l)-min(l))
   if len(set(l)) == 3:
      s = sorted(set(l))
      if s[2]-s[1] == s[1]-s[0]:
         print(s[1]-s[0])
      else:
         print(-1)
      
   
def main():
   # test_cases = int(input())
   
   # for T in range(test_cases):
   #     solution()
      
       #print(f'Case{T+1}:{solution()}')
   solution()

if __name__ == '__main__':
   main()

