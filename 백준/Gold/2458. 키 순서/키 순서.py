import sys
input = sys.stdin.readline

INF = int(1e9)
N, M = map(int,input().split())
G = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int,input().split())
    G[u][v] = 1

for i in range(1, N + 1):
    G[i][i] = 0

for k in range(1, N + 1):
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            G[r][c] = min(G[r][c], G[r][k] + G[k][c])

student = 0
for r in range(1, N + 1):
    count = 0
    for c in range(1, N + 1):
         if (G[r][c] != INF and G[r][c] != 0) or (G[c][r] != INF and G[c][r] != 0):
            count += 1
    if count == N - 1 : student += 1

print(student)