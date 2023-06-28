import sys;
input = sys.stdin.readline

N = int(input())
M = int(input())
G = [[0xffffffff] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    r, c, w = map(int,input().split())
    G[r][c] = min(G[r][c],w)

for k in range(1, N + 1):
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if r == c: G[r][c] = 0
            G[r][c] = min(G[r][c], G[r][k] + G[k][c])

for r in range(1, N + 1):
    for c in range(1, N + 1):
        if G[r][c] == 0xffffffff:
            print(0, end=" ")
        else:
            print(G[r][c], end=" ")
    print()