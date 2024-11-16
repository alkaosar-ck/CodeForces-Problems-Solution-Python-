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
   
   # SINGLE_STR = lambda:input().strip()
   # MINGLE_STR = lambda:map(str,input().split())
   
   LIST_INT = lambda:list(map(int,input().split()))
   #LIST_INT2 = lambda:list(map(int,input().split()))
   # LIST_STR = lambda:list(map(str,input().split()))
   
   # LIST_SORTED = lambda:sorted(list(map(int,input().split())))
   
   return SINGLE_INT(),LIST_INT()
    
    
def find(n, p):
   cycle_lengths = [0] * n 
   for i in range(n):
      if cycle_lengths[i] == 0:
         pos = i 
         ans = 1 
         while p[pos] - 1 != i: 
            ans += 1
            pos = p[pos] - 1 
            
         pos = i 
         for _ in range(ans):
            cycle_lengths[pos] = ans 
            pos = p[pos] - 1 
   return cycle_lengths
def solution():
   n, p = INPUTS()
   cycle_lengths = find(n, p)
   print(' '.join(map(str, cycle_lengths)))

def main():
   test_cases = int(input())
   
   for T in range(test_cases):
       solution()
      
       #print(f'Case{T+1}:{solution()}')
   #solution()

if __name__ == '__main__':
   main()

