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


def solution():
   n = INPUTS()
   if n<2020:
      print('NO')
      return
   c2021 = n%2020
   c2020 = (n-c2021)//2020 -c2021
   if c2020>=0 and 2020*c2020+2021*c2021==n:
      print('YES')
   else:
      print('NO')
   
   
def main():
   test_cases = int(input())
   
   for T in range(test_cases):
       solution()
      
       #print(f'Case{T+1}:{solution()}')
   #solution()

   
   
if __name__ == '__main__':
   main()
