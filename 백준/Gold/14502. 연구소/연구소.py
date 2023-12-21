import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def BFS(virus, unsafe):
    Q = deque(virus)
    area = unsafe
    vi = [[1 if G[n][m] == 1 else 0 for m in range(M)] for n in range(N)]
    for r, c in walls: vi[r][c] = 1
    for r, c in Q : vi[r][c] = 2

    while Q:
        r, c = Q.popleft()
        for dr, dc in ((0, 1),(1, 0),(0, -1),(-1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not vi[nr][nc]:
                Q.append((nr,nc))
                vi[nr][nc] = 1
                area += 1
                if Min <= area : return N * M

    return area

N, M = map(int,input().split())
virus, roads, G = [], [], []
unsafe, Min = 3, N * M

for r in range(N):
    tmp = list(map(int,input().split()))
    G.append(tmp)
    for c in range(M):
        if tmp[c] == 2 : virus.append((r,c)) ; unsafe += 1
        elif tmp[c] == 0 : roads.append((r,c)) ;
        else : unsafe += 1

for walls in combinations(roads,3):
    Min = min(Min,BFS(virus, unsafe))

print(N*M - Min)