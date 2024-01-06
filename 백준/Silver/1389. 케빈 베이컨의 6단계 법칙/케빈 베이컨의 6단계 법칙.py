import sys
input = sys.stdin.readline

INF = int(1e9)
N, M = map(int,input().split())
G = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    G[a][b] = G[b][a] = 1

for i in range(N):
    G[i][i] = 0

for k in range(1,N + 1):
    for r in range(1,N + 1):
        for c in range(1,N + 1):
            if r != c :
                G[r][c] = min(G[r][c],G[r][k] + G[k][c])

people = [0] * (N + 1)
for r in range(1, N + 1):
    for c in range(1, N + 1):
        if r != c:
            people[r] += G[r][c]

for i in range(1, N + 1):
    if people[i] == min(people[1:]):print(i) ; break