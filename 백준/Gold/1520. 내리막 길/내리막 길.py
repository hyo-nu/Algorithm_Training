N, M = map(int,input().split())
G = [[0] * (M + 2)] + [[0] + list(map(int,input().split())) + [0] for _ in range(N)] +[[0] * (M + 2)]
dp = [[-1] * (M + 2) for _ in range(N + 2)]
dp[1][1] = 1

def DFS(r,c):
    if dp[r][c] == -1:
        dp[r][c] = 0
        for dr, dc in ((1,0),(0,1),(-1,0),(0,-1)):
            nr, nc = r + dr, c + dc
            if G[nr][nc] > G[r][c]:
                dp[r][c] += DFS(nr,nc)

    return dp[r][c]
print(DFS(N,M))