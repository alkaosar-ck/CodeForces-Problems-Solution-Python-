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
   #u, v, w = map(int,input().split())
   n, k = map(int, input().split())
   #t = int(input())
   #s = input().strip()
   #s1 = input().strip()
   #s2= input().strip()
   #a,b = input().split()
   #L = sorted(list(map(int, input().split())))
   #H = list(map(int,input().split()))
   #teams = [input().strip().split() for _ in range(n)]
   return n,k
    
    
    
def solution():
    n,s = INPUTS()
    if n%2 == 0:
       t = floor(n/2)-1
       print(floor(s/(n-t)))
       
    else:
       t = floor(n/2)
       print(floor(s/(n-t)))
    
    
def main():
   test_cases = int(input())
   for T in range(test_cases):
       solution()
      
       #print(f'Case{T+1}:{solution()}')
   #solution()

if __name__ == '__main__':
   main()

