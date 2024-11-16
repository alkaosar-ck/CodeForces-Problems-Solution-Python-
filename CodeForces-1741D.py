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
   n = int(sys.stdin.readline().strip())
   #arrary = [int(sys.stdin.readline().strip()) for _ in range(n)]
   #u, v, w = map(int,input().split())
   #n, k = map(int, input().split())
   #t = int(input())
   #s = input().strip()
   #s1 = input().strip()
   #a,b = input().split()
   #L = sorted(list(map(int, input().split())))
   H = list(map(int,input().split()))
   #teams = [input().strip().split() for _ in range(n)]
   return n,H
    
    
def solve_segment(array:List[int],l:int,r:int)->int:
    if r-l == 1:
        return 0
    mid = (r+l)//2
    MxL = max(array[l:mid])
    MxR = max(array[mid:r])
    answer =0
    if MxL>MxR:
        
        answer+=1
        
        array[l:mid], array[mid:r] = array[mid:r], array[l:mid]
        
    return solve_segment(array,l,mid)+solve_segment(array,mid,r)+answer
    
    
def solution():
    n, tree = INPUTS()
    ans = solve_segment(tree,0,n)
    if tree == sorted(tree):
        return ans
    return -1

def main():
   test_cases = int(input())
   for T in range(test_cases):
      print(solution())
      
      #print(f'Case{T+1}:{solution()}')
   #solution()

if __name__ == '__main__':
   main()

