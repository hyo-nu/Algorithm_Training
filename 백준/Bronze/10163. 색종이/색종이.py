N = int(input()) # N <= 10
num = 0
Map = [[0] * 1001 for _ in range(1001)]

for n in range(N):
    RS,CS,W,H = map(int,input().split())
    num += 1
    for r in range(RS,RS + W):
        for c in range(CS,CS + H):
            Map[r][c] = num

for i in range(1,N+1):
    cnt = 0
    for r in range(1001):
        for c in range(1001):
            if Map[r][c] == i:
                cnt += 1
    print(cnt)