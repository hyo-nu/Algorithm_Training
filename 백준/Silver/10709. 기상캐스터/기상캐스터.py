H, W = map(int,input().split())

G = [[-1] * W for _ in range(H)]
sky = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if sky[i][j] == 'c':
            G[i][j] = 0

for i in range(H):
    for j in range(1,W):
        if G[i][j-1] != -1 and G[i][j] == -1:
            G[i][j] = G[i][j-1] + 1
for lst in G:
    print(*lst)