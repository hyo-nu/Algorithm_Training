import sys
input = sys.stdin.readline
from collections import deque

def BFS(r,c):
    Q = deque([(r,c)])
    G[r][c] = 0
    wide = 1

    while Q:
        r,c = Q.popleft()
        for dr,dc in ((0,1),(1,0),(-1,0),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr <N and 0 <= nc <M and G[nr][nc]:
                Q.append((nr,nc))
                G[nr][nc] = 0
                wide += 1
    return wide

N, M = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(N)]

max_wide = count = 0
for r in range(N):
    for c in range(M):
        if G[r][c] :
            max_wide = max(max_wide,BFS(r,c))
            count += 1

print(count,max_wide)