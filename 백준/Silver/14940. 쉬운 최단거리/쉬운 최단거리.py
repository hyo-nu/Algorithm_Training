import sys
input = sys.stdin.readline
from collections import deque

def BFS():
    while Q:
        r,c = Q.popleft()
        for dr,dc in ((0,1),(1,0),(-1,0),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr <N and 0 <= nc <M and G[nr][nc] == -1:
                Q.append((nr,nc))
                G[nr][nc] = G[r][c] + 1

N, M = map(int,input().split())
Q = deque()
G = []

for r in range(N):
    tmp = list(map(int,input().split()))
    for c in range(M):
        if tmp[c] == 2 : Q.append((r,c)) ; tmp[c] = 0
        elif tmp[c] == 1 : tmp[c] = -1
    G.append(tmp)

BFS()
for lst in G:
    print(*lst)