import sys
input = sys.stdin.readline

INF = int(1e9)
V, E = map(int,input().split())
G = [[INF] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    sp, ep, weight = map(int,input().split())
    G[sp][ep] = weight

Min = INF
for k in range(1, V + 1):
    for r in range(1, V + 1):
        for c in range(1, V + 1):
            if r == c : G[r][c] = 0
            G[r][c] = min(G[r][c],G[r][k] + G[k][c])
            if r != c : Min = min(Min, G[r][c] + G[c][r])

print(Min if Min != INF else -1)