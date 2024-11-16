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
   #n, k = map(int, input().split())
   #t = int(input())
   s = input().strip()
   s1 = input().strip()
   s2= input().strip()
   #a,b = input().split()
   #L = sorted(list(map(int, input().split())))
   #H = list(map(int,input().split()))
   #teams = [input().strip().split() for _ in range(n)]
   return s,s1,s2
    
def name(n):
    if n == 0:
        return 'F'
    if n == 1:
        return 'M'
    if n == 2:
        return 'S'
    
    
def solution():
    F,M,S= INPUTS()
    l = [F,M,S]
    rocks = l.count('rock')
    scissors = l.count('scissors')
    paper = l.count('paper')
    
    if rocks>0 and paper>0:
        if paper ==1 and 2 == rocks:
            p = (l.index('paper'))
            print(name(p))
            return
    if rocks>0 and scissors>0:
        if rocks ==1 and  2 == scissors:
            p = (l.index('rock'))
            print(name(p))
            return
    if scissors>0 and paper>0:
        if scissors ==1 and  2 == paper:
            p = (l.index('scissors'))
            print(name(p))
            return
    print('?')
    
        
    
    
def main():
#    test_cases = int(input())
#    for T in range(test_cases):
#        solution()
      
       #print(f'Case{T+1}:{solution()}')
   solution()

if __name__ == '__main__':
   main()

