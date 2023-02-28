N = int(input()) # N <= 10
num = 0
Map = [[0] * 1001 for _ in range(1001)]

cnt = []
rs = cs = re = ce = 0
for n in range(N):
    R,C,W,H = map(int,input().split())
    num += 1
    if re < R + W : re = R + W
    if ce < C + H : ce = C + H
    if rs > R : rs = R
    if cs > C : cs = C
    for r in range(R,R + W):
        for c in range(C,C + H):
            Map[r][c] = num

for i in range(1,N+1):
    cnt = 0
    for r in range(rs,re):
        for c in range(cs,ce):
            if Map[r][c] == i:
                cnt += 1
    print(cnt)