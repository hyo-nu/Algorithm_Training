import sys
from collections import deque
input = sys.stdin.readline

def find(sp):
    if sp != parent[sp]:
        parent[sp] = find(parent[sp])
    return parent[sp]

def union(sp, ep):
    parent[find(sp)] = find(ep)

N = int(input())
parent = [i for i in range(N + 1)]
G = []
for r in range(N):
    star = list(map(int, input().split()))
    for c in range(N):
        if r < c : G.append((r,c,star[c]))

G.sort(key = lambda x : x[2])

Min = edge = 0
for sp, ep, weight in G:
    if find(sp) != find(ep):
        Min += weight
        edge += 1
        union(sp, ep)
        if edge == N-1:
            break
print(Min)