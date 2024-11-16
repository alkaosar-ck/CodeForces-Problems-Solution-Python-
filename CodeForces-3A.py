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
   #a,b = input().split()
   #L = sorted(list(map(int, input().split())))
   #H = list(map(int,input().split()))
   #teams = [input().strip().split() for _ in range(n)]
   return s,s1
    
    
    
def solution():
    answer = []
    now, target = INPUTS()
    
    now_col, now_row = now[0], int(now[1])
    target_col, target_row = target[0], int(target[1])
    
    while (now_col, now_row) != (target_col, target_row):
        current_move = ''
        
        # Diagonal movement: LU, LD, RU, RD
        if now_col > target_col and now_row < target_row:
            current_move = 'LU'
            now_col = chr(ord(now_col) - 1)
            now_row += 1
            
            
        elif now_col > target_col and now_row > target_row:
            current_move = 'LD'
            now_col = chr(ord(now_col) - 1)
            now_row -= 1
            
            
        elif now_col < target_col and now_row < target_row:
            current_move = 'RU'
            now_col = chr(ord(now_col) + 1)
            now_row += 1
            
            
        elif now_col < target_col and now_row > target_row:
            current_move = 'RD'
            now_col = chr(ord(now_col) + 1)
            now_row -= 1
            
            
        else:
            # Horizontal movement: Left (L) or Right (R)
            if now_col > target_col:
                current_move = 'L'
                now_col = chr(ord(now_col) - 1)
                
                
            elif now_col < target_col:
                current_move = 'R'
                now_col = chr(ord(now_col) + 1)
            
            # Vertical movement: Down (D) or Up (U)
            if now_row > target_row:
                current_move = 'D'
                now_row -= 1
            elif now_row < target_row:
                current_move = 'U'
                now_row += 1
        answer.append(current_move)
        
    print(len(answer))
    for x in answer:
        print(x)

def main():
   #test_cases = int(input())
#    for T in range(test_cases):
#       solution()
      
#       #print(f'Case{T+1}:{solution()}')
   solution()

if __name__ == '__main__':
   main()

