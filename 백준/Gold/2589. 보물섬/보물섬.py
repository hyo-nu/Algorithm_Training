import sys
from collections import deque

input = sys.stdin.readline

def BFS(sr, sc):
    Q = deque([(sr,sc)])
    vi = [[-1] * M for _ in range(N)]
    vi[sr][sc] = 0
    Max = 0
    while Q:
        r, c = Q.popleft()
        for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
            if 0 <= (nr:= r + dr) < N and 0 <= (nc := c+dc) < M:
                if G[nr][nc] == "L" and vi[nr][nc] == -1 :
                    Q.append((nr, nc))
                    vi[nr][nc] = vi[r][c] + 1
                    Max = max(Max, vi[nr][nc])
    return Max

N, M = map(int,input().split())
G, lands = [], []
for r in range(N):
    tmp = list(input().rstrip())
    G.append(tmp)
    for c in range(M):
        if tmp[c] == "L" : lands.append((r,c))

result = 0
for sr, sc in lands:
    result = max(result,BFS(sr, sc))
print(result)
