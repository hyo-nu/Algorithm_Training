import sys;
input = sys.stdin.readline

INF = 1000
N, M = map(int,input().split())
G = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    sp, ep = map(int,input().split())
    G[sp][ep] = 1
    G[ep][sp] = 1

for r in range(1, N + 1):
    G[r][r] = 0

for k in range(1, N + 1):
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if r == c : continue
            G[r][c] = min(G[r][c], G[r][k] + G[k][c])

Min = N * 1000
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        h1, h2 = G[i], G[j]
        tmp = 0
        for k in range(1, N + 1):
            tmp += min(G[i][k], G[j][k])

        if Min > tmp:
            Min = tmp
            r, c = i, j

print(r, c, Min*2)