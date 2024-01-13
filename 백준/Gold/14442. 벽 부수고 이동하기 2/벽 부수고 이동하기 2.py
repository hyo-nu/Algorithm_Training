import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while Q:
        r, c, z = Q.popleft()
        if r == N - 1 and c == M - 1:
            return vi[r][c][z]
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M :
                if G[nr][nc] == 1  and z < K and vi[nr][nc][z+1] == 0:
                    vi[nr][nc][z+1] = vi[r][c][z] + 1
                    Q.append((nr,nc,z+1))

                elif G[nr][nc] == 0 and vi[nr][nc][z] == 0:
                    vi[nr][nc][z] = vi[r][c][z] + 1
                    Q.append((nr,nc,z))

    return -1

N, M, K = map(int,input().split())
G = [list(map(int,input().rstrip())) for _ in range(N)]
vi = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
vi[0][0][0] = 1

Q = deque([(0, 0, 0)])
print(bfs())