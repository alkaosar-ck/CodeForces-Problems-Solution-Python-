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
   #s = input().strip()
   #s1 = input().strip()
   #a,b = input().split()
   #L = sorted(list(map(int, input().split())))
   H = list(map(int,input().split()))
   #teams = [input().strip().split() for _ in range(n)]
   return H
    
def dfs(grid,visited,i,j,n,m):
    stack = [(i,j)]
    volume = 0
    while stack:
        x,y = stack.pop()
        if visited[x][y]:
            continue
        visited[x][y] = True
        volume+=grid[x][y]
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and grid[nx][ny]>0:
                stack.append((nx,ny))
    return volume

    
def solution(n,m):
    matrix = []
    for x in range(n):
        matrix.append(INPUTS())
    visited = [[False]*m for _ in range(n)]
    max_volume = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j]>0 and not visited[i][j]:
                lake_volume = dfs(matrix,visited,i,j,n,m)
                max_volume = max(max_volume,lake_volume)
    print(max_volume)
def main():
   test_cases = int(input())
   for T in range(test_cases):
       n,m = map(int,input().split())
       solution(n,m)
      
#       #print(f'Case{T+1}:{solution()}')
   #solution()

if __name__ == '__main__':
   main()

