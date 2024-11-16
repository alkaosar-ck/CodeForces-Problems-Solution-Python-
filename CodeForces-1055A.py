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
   MINGLE_INT = lambda:map(int,input().split())
   
   # SINGLE_STR = lambda:input().strip()
   # MINGLE_STR = lambda:map(str,input().split())
   
   LIST_INT = lambda:list(map(int,input().split()))
   LIST_INT2 = lambda:list(map(int,input().split()))
   # LIST_STR = lambda:list(map(str,input().split()))
   
   # LIST_SORTED = lambda:sorted(list(map(int,input().split())))
   
   return MINGLE_INT(),LIST_INT(),LIST_INT2()
    
    
    
def solution():
    d,going,coming = INPUTS()
    n,s = d
    if going[0] == 1 and going[s-1] == 1:
       print('YES')
       return
    elif going[0] == 0 :
       print("NO")
       return
    elif going[s-1] and coming[s-1]:
       print('YES')
       return
    for k in range(s,n):
       if going[k] == 1 and coming[k] == 1 and coming[s-1] == 1:
          print('YES')
          return
    print("NO")
    
         
   
        
def main():
   # test_cases = int(input())
   
   # for T in range(test_cases):
   #     solution()
      
       #print(f'Case{T+1}:{solution()}')
   solution()

if __name__ == '__main__':
   main()

