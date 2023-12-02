from heapq import heappop, heappush

INF = 1e9
order = 0
while True:
    N = int(input())
    if not N : break
    order += 1
    G = [list(map(int,input().split())) for _ in range(N)]

    h = []
    heappush(h,(0,0,0))
    Distance = [[INF] * N for _ in range(N)]
    Distance[0][0] = G[0][0]

    while h :
        start_distance, r, c = heappop(h)
        if Distance[r][c] < start_distance : continue

        for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if Distance[nr][nc] > Distance[r][c] + G[nr][nc]:
                    Distance[nr][nc] = Distance[r][c] + G[nr][nc]
                    heappush(h,(Distance[r][c] + G[nr][nc], nr, nc))

    print("Problem {}: {}".format(order,Distance[N-1][N-1]))