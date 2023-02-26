from collections import deque
def Multi_BFS(Q):
    dr = [0, 1, 0,-1, N,-N] #우,하,좌,상,위,아래
    dc = [1, 0,-1, 0, 0, 0]
    Max = 0
    cnt = 0
    while Q:
        r,c = Q.popleft()
        for d in range(6):
            nr = r + dr[d]
            nc = c + dc[d]
            if d <= 3:
                tmpr = (r % N) + dr[d]
                if 0 <= tmpr < N and 0 <= nc < M and mato[nr][nc] == -1:
                    mato[nr][nc] = mato[r][c] + 1
                    Q.append((nr, nc))
                    if Max < mato[nr][nc]:
                        Max = mato[nr][nc]
            elif d > 3:
                if 0 <= nr < N * H and 0 <= nc < M and mato[nr][nc] == -1:
                    mato[nr][nc] = mato[r][c] + 1
                    Q.append((nr, nc))
                    if Max < mato[nr][nc]:
                        Max = mato[nr][nc]


    for lst in mato:
        cnt += lst.count(-1)
    if cnt != 0 : return -1
    else : return Max

M,N,H = map(int,input().split())
mato = [[-1]*M for _ in range(N * H)]

# 토마토 받아오기
Q = deque()
cnt = 0

for r in range(N * H):  # N 세로
    to = list(map(int,input().split()))
    for c in range(M): # M 가로
        if to[c] == 1 : mato[r][c] = 0 ; Q.append((r,c))
        elif to[c] == -1 : mato[r][c] = -2
        elif to[c] == 0 : cnt += 1

if cnt == 0 : print(0) # 덜익은 토마토 없는경우
else : print(Multi_BFS(Q))