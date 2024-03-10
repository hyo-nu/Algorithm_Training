import sys;
input = sys.stdin.readline

N, M = int(input()), int(input())
G = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    sp, ep = map(int,input().split())
    G[sp][ep] = 1
    G[ep][sp] = -1

for k in range(1, N + 1):
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if r == c : continue
            if G[r][k] == -1 and  G[k][c] == -1 : G[r][c] = -1
            elif G[r][k] == 1 and  G[k][c] == 1 : G[r][c] = 1

for r in range(1,N + 1):
    cnt = 0
    for c in range(1,N + 1):
        if r == c : continue
        if G[r][c] == 0 : cnt += 1

    print(cnt)