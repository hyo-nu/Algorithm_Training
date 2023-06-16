from collections import deque

def BFS1():
    Q = deque()
    Q.append((0,0))
    vi = [[0] * C for _ in range(R)]
    vi[0][0] = 1
    while Q:
        r, c = Q.popleft()
        for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and G[nr][nc] == 0:
                if not vi[nr][nc]:
                    vi[nr][nc] = 1
                    Q.append((nr,nc))
    return vi

def BFS2(vi):
    count = 0
    for r in range(R):
        for c in range(C):
            if G[r][c] == 1:
                count += 1
                for vr, vc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    if vi[r + vr][c + vc] == 1:
                        Q = deque()
                        Q.append((r,c))
                        G[r][c] = 0
                        while Q:
                            rr, cc = Q.popleft()
                            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                                nr, nc = rr + dr, cc + dc
                                if 0 <= nr < R and 0 <= nc < C and G[nr][nc] == 1:
                                    for vr,vc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                                        if vi[nr+vr][nc+vc] == 1:
                                            G[nr][nc] = 0
                                            Q.append((nr,nc))
                                            count += 1
                                            break
                        break
    return(count)
R, C = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(R)]
count = []
while True:
    vi = BFS1()
    count.append(BFS2(vi))
    if count[-1] == 0 : break
print(len(count)-1)
print(count[-2])