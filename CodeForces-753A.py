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
   
   #LIST_INT = lambda:list(map(int,input().split()))
   # LIST_INT2 = lambda:list(map(int,input().split()))
   # LIST_STR = lambda:list(map(str,input().split()))
     
   #LIST_SORTED = lambda:sorted(list(map(int,input().split())))
   
   return SINGLE_INT()

def nth_triangular_number(n):
   return (n*(n+1))//2


def LOWER_BOUND(n):
    left, right = 0, n
    while left < right:
        mid = (left + right + 1) // 2 
        if nth_triangular_number(mid) <= n:
            left = mid  
        else:
            right = mid - 1 
    return left


def solution():
   n= INPUTS()
   t = LOWER_BOUND(n)
   print(t)
   if t == 1:
      print(n)
      return
   answer = []
   s = 0
   for x in range(1,t):
      answer.append(x)
      s+=x
   r = n-s
   answer.append(r)
   print(*answer)
   
   
def main():
   # test_cases = int(input())
   
   # for T in range(test_cases):
   #     solution()
      
       #print(f'Case{T+1}:{solution()}')
   solution()

   
   
if __name__ == '__main__':
   main()

