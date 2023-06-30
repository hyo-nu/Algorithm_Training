from collections import deque

N, M = map(int,input().split())
G, S = [], []

for r in range(N):
    lst = list(map(int,input().split()))
    G.append(lst)
    for c in range(M):
        if lst[c] == 1 :
            S.append((r,c))

Q = deque()
for r,c in S:
    Q.append((r,c))

    def BFS():
        global safezone
        vi = [[0] * M for _ in range(N)]
        for R, C in S:
            vi[R][C] = 1

        while Q :
            r,c = Q.popleft()
            for dr, dc in ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and not vi[nr][nc]:
                    if not G[nr][nc] or G[nr][nc] > G[r][c]:
                        G[nr][nc] = G[r][c] + 1
                        Q.append((nr,nc))
                        vi[nr][nc] = 1
    BFS()

print(max([max(lst) for lst in G])-1)
