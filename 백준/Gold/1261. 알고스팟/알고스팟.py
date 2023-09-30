from heapq import heappop, heappush

M, N = map(int,input().split())
INF = int(1e9)
G = []
for r in range(N):
    tmp = list(map(int,input()))
    for c in range(M):
        if tmp[c] == 1 : tmp[c] = INF
    G.append(tmp)

h = []
r, c = 0, 0
heappush(h,(1,r,c))
G[r][c] = 1

while h:
    now_distancd,r,c = heappop(h)
    if G[r][c] and G[r][c] < now_distancd : continue

    for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if not G[nr][nc] :
                G[nr][nc] = G[r][c]
                heappush(h, (G[r][c], nr, nc))

            elif G[nr][nc] and G[nr][nc] > G[r][c] + 1:
                G[nr][nc] = G[r][c] + 1
                heappush(h,(G[r][c] + 1,nr,nc))

print(G[N-1][M-1]-1)