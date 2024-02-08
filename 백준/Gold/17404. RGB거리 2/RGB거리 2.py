import sys;
input = sys.stdin.readline

N = int(input())
INF = int(1e9)
G = [list(map(int,input().split())) for _ in range(N)]
GR = [G[0][0] + G[1][i] for i in range(3)]
GG = [G[0][1] + G[1][i] for i in range(3)]
GB = [G[0][2] + G[1][i] for i in range(3)]
GR[0] = INF
GG[1] = INF
GB[2] = INF
DPR = [INF] * 3
DPG = [INF] * 3
DPB = [INF] * 3

for r in range(2, N):
    for c in range(3):
        MinR = MinG = MinB = INF
        for k in range(3):
            if c != k :
                MinR = min(MinR, GR[k])
                MinG = min(MinG, GG[k])
                MinB = min(MinB, GB[k])
        DPR[c] = G[r][c] + MinR
        DPG[c] = G[r][c] + MinG
        DPB[c] = G[r][c] + MinB
    for i in range(3):
        GR[i] = DPR[i]
        GG[i] = DPG[i]
        GB[i] = DPB[i]

result = INF
for i in range(N):
    if i == 0 : result = min(result, DPR[1], DPR[2])
    elif i == 1: result = min(result, DPG[0], DPG[2])
    elif i == 2 : result = min(result, DPB[0], DPB[1])

print(result)