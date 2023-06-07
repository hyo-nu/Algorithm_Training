from collections import deque

def BFS(r,c):
    global size
    Q = deque()
    Q.append((r,c))
    G[r][c] = 0
    while Q:
        r,c = Q.popleft()
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and G[nr][nc] == 1:
                Q.append((nr,nc))
                G[nr][nc] = 0
                size += 1

N, M, K = map(int,input().split())
G = [[0] * M for _ in range(N)]

for _ in range(K):
    r,c = map(int,input().split())
    G[r-1][c-1] = 1

Max_size = 0
for r in range(N):
    for c in range(M):
        if G[r][c] == 1:
            size = 1
            BFS(r,c)
            Max_size = max(Max_size,size)
print(Max_size)
