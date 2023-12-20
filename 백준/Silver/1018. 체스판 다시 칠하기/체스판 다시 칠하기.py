def Check_white(sr,sc):
    chagne = 0
    for r in range(8):
        for c in range(8):
            if (sr + r + sc + c) % 2 and G[sr+r][sc+c] != "W":chagne += 1
            elif not (sr + r + sc + c) % 2 and G[sr+r][sc+c] != "B":chagne += 1
    return chagne

def Check_black(sr,sc):
    chagne = 0
    for r in range(8):
        for c in range(8):
            if (sr + r + sc + c) % 2 and G[sr+r][sc+c] != "B":chagne += 1
            elif not (sr + r + sc + c) % 2 and G[sr+r][sc+c] != "W":chagne += 1
    return chagne

N, M = map(int,input().split())
G = [list(input()) for _ in range(N)]

Min = 1e9
for sr in range(N-7):
    for sc in range(M-7):
        Min = min(Min,Check_white(sr,sc))
        Min = min(Min,Check_black(sr,sc))
print(Min)