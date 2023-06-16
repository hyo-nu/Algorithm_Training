N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * (N) for _ in range(N)]
dp[0][0] = 1

for r in range(N):
    for c in range(N):
        if dp[r][c] and G[r][c] and r + G[r][c] < N:
            dp[r + G[r][c]][c] += dp[r][c]
        if dp[r][c] and G[r][c] and c + G[r][c] < N:
            dp[r][c + G[r][c]] += dp[r][c]
print(dp[N-1][N-1])