from collections import deque
from itertools import combinations
from copy import deepcopy

def BFS(arr,lst):
    safe = 0
    q = deque(lst)
    while q:
        r, c = q.popleft()
        for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                q.append((nr,nc))
                arr[nr][nc] = 1

    for lst in arr:
        safe += lst.count(0)
    return safe

N, M = map(int,input().split())
G = []
Q = deque()
empty = []
for r in range(N):
    tmp = list(map(int,input().split()))
    G.append(tmp)
    for c in range(M):
        if tmp[c] == 2 : Q.append((r,c))
        if tmp[c] == 0 : empty.append((r,c))

Max = 0
for lst in combinations(empty, 3):
    G_copy = deepcopy(G)
    for R, C in lst:
        G_copy[R][C] = 1
    Max = max(Max,BFS(G_copy,Q))

print(Max)