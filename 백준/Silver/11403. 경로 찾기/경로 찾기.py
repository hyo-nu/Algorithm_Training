N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for r in range(N):
        for c in range(N):
            if G[r][k] and G[k][c] :
                G[r][c] = 1

for lst in G:
    print(*lst)