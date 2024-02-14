import sys;
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int,input().split())
route = [[0] * n for _ in range(n)]
G = [[INF] * n for _ in range(n)]

for _ in range(m):
    sp, ep, weight = map(int,input().split())
    G[sp-1][ep-1] = weight
    G[ep-1][sp-1] = weight
    route[sp-1][ep-1] = ep
    route[ep-1][sp-1] = sp

for k in range(n):
    for r in range(n):
        for c in range(n):
            if r == c :
                G[r][c] = 0
                route[r][c] = "-"
            else:
                if G[r][c] > G[r][k] + G[k][c]:
                    G[r][c] = G[r][k] + G[k][c]
                    route[r][c] = k + 1
                    dc = c
                    while route[r][dc]-1 != dc:
                        dc = route[r][dc] - 1
                    route[r][c] = dc + 1

for lst in route:print(*lst)