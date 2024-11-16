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
   
   #SINGLE_STR = lambda:input().strip()
   # MINGLE_STR = lambda:map(str,input().split())
   
   #LIST_INT = lambda:list(map(int,input().split()))
   #LIST_INT2 = lambda:list(map(int,input().split()))
   # LIST_STR = lambda:list(map(str,input().split()))
     
   #LIST_SORTED = lambda:sorted(list(map(int,input().split())))
   
   return MINGLE_INT()
      
def solution():
    n = int(input())
    chemforces = {}
    for i in range(1, n + 1):
        ai, xi = map(int, input().split())
        chemforces[ai] = xi

    m = int(input())
    topchemist = {}
    for i in range(n + 2, n + 2 + m):
        bj, yj = map(int, input().split())
        topchemist[bj] = yj

    total_income = 0
    seen_indices = set(chemforces.keys()).union(topchemist.keys())

    for index in seen_indices:
        income_chemforces = chemforces.get(index, 0)
        income_topchemist = topchemist.get(index, 0)
        total_income += max(income_chemforces, income_topchemist)

    print(total_income)

            
   
def main():
   # test_cases = int(input())
   
   # for T in range(test_cases):
   #     solution()
      
       #print(f'Case{T+1}:{solution()}')
   solution()

   
   
if __name__ == '__main__':
   main()
