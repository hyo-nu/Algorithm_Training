import sys;
input = sys.stdin.readline

H, W = map(int,input().split())
blocks = list(map(int,input().split()))
G = [[0] * W for _ in range(H)]

for c in range(len(blocks)):
    for r in range(blocks[c]):
        G[r][c] = 1

result = 0
for r in range(H):
    for c in range(W):
        if G[r][c] != 0: continue

        start = end = 0
        for k in range(W):
            if G[r][k] == 0 : continue
            if k < c : start = 1
            else : end = 1

        if start == 1 and end == 1 : result += 1

print(result)
