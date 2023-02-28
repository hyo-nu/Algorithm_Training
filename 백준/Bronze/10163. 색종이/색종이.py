
N = int(input()) # N <= 10
num = 0
Map = [[0] * 1001 for _ in range(1001)]

cnt = []
R = C = 0
for n in range(N):
    RS,CS,W,H = map(int,input().split())
    num += 1
    if R < RS + W : R = RS + W
    if C < CS + H : C = CS + H
    for r in range(RS,RS + W):
        for c in range(CS,CS + H):
            Map[r][c] = num

for i in range(1,N+1):
    cnt = 0
    for r in range(R):
        for c in range(C):
            if Map[r][c] == i:
                cnt += 1
    print(cnt)