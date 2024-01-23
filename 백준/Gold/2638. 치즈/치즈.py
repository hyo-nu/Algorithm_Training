import sys
input = sys.stdin.readline
from collections import deque

def contactAir():
    airs = [[0] * M for _ in range(N)]
    Q = deque([(0,0)])
    airs[0][0] = -1
    while Q:
        r,c = Q.popleft()
        for dr, dc in ((0,1),(1,0),(-1,0),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M :
                if G[nr][nc] == 0 and airs[nr][nc] != -1:
                    Q.append((nr, nc))
                    airs[nr][nc] = -1
    return airs

def BFS(r,c,airs):
    global stop
    contact_cnt = 0
    stop = 0
    for dr, dc in ((0,1),(1,0),(-1,0),(0,-1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M :
            if G[nr][nc] == 0 and airs[nr][nc] == -1:
                contact_cnt += 1

    if contact_cnt >= 2:
        G[r][c] = 0

N, M = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(N)]
cycle = 0

while True:
    airs = contactAir()
    cycle += 1
    stop = 1
    for r in range(1, N-1):
        for c in range(1, M-1):
            if G[r][c] == 1:
                BFS(r,c,airs)
    if stop : break

print(cycle-1)