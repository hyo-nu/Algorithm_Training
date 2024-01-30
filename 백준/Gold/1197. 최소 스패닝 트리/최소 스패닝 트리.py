import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def find_parent(sp):
    if sp != parent[sp]:
        parent[sp] = find_parent(parent[sp])
    return parent[sp]

def union(sp, ep):
    parent[find_parent(sp)] = find_parent(ep)

N, M = map(int,input().split())
parent = [i for i in range(N + 1)]
edge = []

for _ in range(M):
    sp, ep, weight = map(int,input().split())
    edge.append((sp, ep, weight))

edge.sort(key = lambda x : x[2])

MST = 0
for sp, ep, weight in edge:
    if find_parent(sp) != find_parent(ep):
        MST += weight
        union(sp,ep)

print(MST)