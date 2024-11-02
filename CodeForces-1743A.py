from collections import *
from math import *
from heapq import *
from itertools import *
from queue import *
from cmath import *
from random import *
from functools import *
from time import *
import sys
import os
import decimal

def Seive(LIMIT):
   T = int(sqrt(abs(LIMIT)))+1
   primes = [True]*(T+1)
   primes[0]=primes[1]=False
   for i in range(2,T+1):
      if primes[i]:
         for q in range(i+i,LIMIT+1,i):
            primes[q] = False
   return [p for p in range(LIMIT) if primes[p]]

def prime(n):
   factors = Seive(n)
   possible = True
   for x in factors:
      if n%x == 0:
         possible = False
         break
   return possible

def solution():
   #u,v,w = map(int,input().split())
   #n, k = map(int, input().split())
   t = int(input())
   #s = input().strip()
   #L = sorted(list(map(int, input().split())))
   H = list(map(int,input().split()))
   r = 10-t
   print(r*(r-1)*3)
def main():
   for _ in range(int(input())):
      solution()
   #solution()

if __name__ == '__main__':
   main()