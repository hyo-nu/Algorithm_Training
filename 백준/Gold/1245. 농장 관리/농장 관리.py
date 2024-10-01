from collections import deque

N, M = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(N)]
vi = [[0] * M for _ in range(N)]
result = 0

def BFS(r,c,h):
    q = deque([(r,c,h)])
    vi[r][c] = 0
    flag = 1

    while q :
        sr, sc , sh = q.popleft()
        for dr, dc in ((0,1),(1,0),(0,-1),(-1,0),(-1,1),(1,1),(1,-1),(-1,-1)):
            nr, nc = sr + dr, sc + dc
            if 0 <= nr < N and 0 <= nc < M :
                if vi[nr][nc] == 0 and G[nr][nc] == sh:
                    q.append((nr,nc,G[nr][nc]))
                    vi[nr][nc] = 1

                elif G[nr][nc] > sh :
                    flag = 0

    return flag

for i in range(N):
    for j in range(M):
        if not vi[i][j]:
            result += BFS(i,j,G[i][j])

print(result)