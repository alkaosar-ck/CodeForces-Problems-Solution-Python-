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

def INPUTS():
   # n = int(sys.stdin.readline().strip())
   # arrary = [int(sys.stdin.readline().strip()) for _ in range(n)]
   # u, v, w = map(int,input().split())
   # n, k = map(int, input().split())
   # t = int(input())
   #s = input().strip()
   a,b = input().split()
   # L = sorted(list(map(int, input().split())))
   # H = list(map(int,input().split()))
   return a,b


def solution(Map,current_map):
   old,new = INPUTS()
   if old in Map:
      original = Map[old]
      Map[new] = original
      del Map[old]
   else:
      Map[new] = old


def main():
   Map = {}
   test_cases = int(input())
   for T in range(test_cases):
      solution(Map,{})
   # solution()
   answer = []
   for new,old in Map.items():
      answer.append(f'{old} {new}')
   print(len(answer))
   for line in answer:print(line)
   
def AND(arr):
    result = arr[0]
    for num in arr[1:]:
        result &= num
    return result
 
def OR(arr):
    result = arr[0]
    for num in arr[1:]:
        result |= num
    return result
 
 
def XOR(arr):
    result = arr[0]
    for num in arr[1:]:
        result ^= num
    return result



def Seive(LIMIT):
   T = int(sqrt(abs(LIMIT)))+1
   primes = [True]*(T+1)
   primes[0] = primes[1] = False
   for i in range(2, T+1):
      if primes[i]:
         for q in range(i+i, LIMIT+1, i):
               primes[q] = False
   return [p for p in range(LIMIT) if primes[p]]

def prime(n):
   factors = Seive(n)
   possible = True
   for x in factors:
      if n % x == 0:
         possible = False
         break
   return possible

def PRIME_FACTORS(n):
    factors = [1] 
    if n == 0:
       return
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)

    return factors


def SUBARRAYS(arr):
    n = len(arr)
    subarrays = []
    for start in range(n):
        for end in range(start, n):
            subarrays.append(arr[start:end + 1])
    return subarrays

def SUBSEQUENCES(arr):
    n = len(arr)
    subsequences = []
    for i in range(1 << n):  
        subseq = []
        for j in range(n):
            if i & (1 << j):  
                subseq.append(arr[j])
        subsequences.append(subseq)
    return subsequences


def BFS(graph, start):
   visited = set()
   queue = deque([start])
   result = []

   while queue:
      node = queue.popleft()
      if node not in visited:
         visited.add(node)
         result.append(node)
         for neighbor in graph[node]:
               if neighbor not in visited:
                  queue.append(neighbor)

   return result

def DFS(graph, start):
   visited = set()
   stack = [start]
   result = []

   while stack:
      node = stack.pop()
      if node not in visited:
         visited.add(node)
         result.append(node)
         for neighbor in reversed(graph[node]):
               if neighbor not in visited:
                  stack.append(neighbor)

   return result


def TREE_EDGE_LIST(n, edges):
   tree = {i: [] for i in range(1, n + 1)}
   for u, v in edges:
      tree[u].append(v)
      tree[v].append(u) 
   return tree


def INPUTS_TREE_EDGE_LIST():
   n, m = map(int, input().split())
   edges = [tuple(map(int, input().split())) for _ in range(m)]
   graph = TREE_EDGE_LIST(n, edges) 
   print("Undirected graph from edge list:", graph)


def TREE_ADJ_LIST(adj_list):
   tree = {}
   for node, neighbors in adj_list.items():
      tree[node] = neighbors
   return tree


def GRAPH_ADJ_MATRIX(adj_matrix):
   graph = {}
   n = len(adj_matrix)
   for i in range(n):
      graph[i] = []
      for j in range(n):
         if adj_matrix[i][j] != 0:
               graph[i].append(j)
   return graph


def INPUTS_GRAPH_ADJ_MATRIX():
   n = int(input())
   adj_matrix = [list(map(int, input().split())) for _ in range(n)]
   graph = GRAPH_ADJ_MATRIX(adj_matrix)
   print("Graph from adjacency matrix:", graph)


def GRAPH_INC_MATRIX(inc_matrix):
   graph = {}
   num_vertices = len(inc_matrix)
   num_edges = len(inc_matrix[0])

   for i in range(num_vertices):
      graph[i] = []

   for j in range(num_edges):
      vertices = []
      for i in range(num_vertices):
         if inc_matrix[i][j] == 1:
               vertices.append(i)
      if len(vertices) == 2:
         u, v = vertices
         graph[u].append(v)
         graph[v].append(u)

   return graph

def INPUTS_GRAPH_INC_MATRIX():
   n, m = map(int, input().split())
   inc_matrix = [list(map(int, input().split())) for _ in range(n)]
   graph = GRAPH_INC_MATRIX(inc_matrix)
   print("Graph from incidence matrix:", graph)


def GRAPH_WEIGHTED_EDGE_LIST(n, weighted_edges):
   graph = {i: [] for i in range(1, n + 1)}
   for u, v, weight in weighted_edges:
      graph[u].append((v, weight))
      graph[v].append((u, weight))
   return graph

def INPUTS_WEIGHTED_EDGE_LIST():
   n, m = map(int, input().split())
   weighted_edges = [tuple(map(int, input().split())) for _ in range(m)]
   graph = GRAPH_WEIGHTED_EDGE_LIST(n, weighted_edges)
   print("Weighted graph from edge list:", graph)


def GRAPH_UNDIRECTED_EDGE_LIST(n, edges):
   graph = {i: [] for i in range(1, n + 1)}
   for u, v in edges:
      graph[u].append(v)
      graph[v].append(u)
   return graph

def INPUTS_GRAPH_EDGE_LIST(directed=True):
   n, m = map(int, input().split())
   edges = [tuple(map(int, input().split())) for _ in range(m)]
   if directed:
      graph = GRAPH_DIRECTED_EDGE_LIST(n, edges)
      print("Directed graph from edge list:", graph)
   else:
      graph = GRAPH_UNDIRECTED_EDGE_LIST(n, edges)
      print("Undirected graph from edge list:", graph)


def GRAPH_DIRECTED_EDGE_LIST(n, edges):
   graph = {i: [] for i in range(1, n + 1)}
   for u, v in edges:
      graph[u].append(v)
   return graph




if __name__ == '__main__':
   main()
