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
   
   #SINGLE_INT = lambda:int(input())
   #MINGLE_INT = lambda:map(int,input().split())
   
   SINGLE_STR = lambda:input().strip()
   # MINGLE_STR = lambda:map(str,input().split())
   
   #LIST_INT = lambda:list(map(int,input().split()))
   #LIST_INT2 = lambda:list(map(int,input().split()))
   # LIST_STR = lambda:list(map(str,input().split()))
   
   # LIST_SORTED = lambda:sorted(list(map(int,input().split())))
   
   return SINGLE_STR()
    

def solution():
   n = INPUTS()
   cnt0 = n.count('0')
   cnt1 = n.count('1')
   if '0' in n and '1' not in n:
      print(1)
      return
   if '1' in n and '0' not in n:
      print(0)
      return
   
   total = 0
   
   f = n[0]
   
   for x in n:
      if x != f:
         total+=1
         f = x
   if f == '0' and total>=2:
      print(2)
   elif f == '1' and total>=3:
      print(2)
   else:
      print(1)
      
   
      
      
   
   
def main():
   test_cases = int(input())
   
   for T in range(test_cases):
       solution()
      
       #print(f'Case{T+1}:{solution()}')
   #solution()

if __name__ == '__main__':
   main()

