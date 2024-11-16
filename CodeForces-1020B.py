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
   # MINGLE_INT = lambda:map(int,input().split())
   
   # SINGLE_STR = lambda:input().strip()
   # MINGLE_STR = lambda:map(str,input().split())
   
   LIST_INT = lambda:list(map(int,input().split()))
   # LIST_STR = lambda:list(map(str,input().split()))
   
   # LIST_SORTED = lambda:sorted(list(map(int,input().split())))
   
   return SINGLE_INT(),LIST_INT()
    
def find(n,p):
   result = []
   for a in range(1,n+1):
      visited = set()
      current = a
      while current not in visited:
         visited.add(current)
         current = p[current-1]
      result.append(current)
   print(' '.join(map(str,result)))
   
    
    
def solution():
    l,p = INPUTS()
    find(l,p)
         
   
        
def main():
   # test_cases = int(input())
   
   # for T in range(test_cases):
   #     solution()
      
       #print(f'Case{T+1}:{solution()}')
   solution()

if __name__ == '__main__':
   main()

