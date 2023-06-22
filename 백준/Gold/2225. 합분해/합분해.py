N, K = map(int,input().split())
dp = [0] * (N + 1)

for k in range(K):
    for n in range(N+1):
        if n == 0 or k == 0: dp[n] = 1
        else:
            dp[n] += dp[n-1]

print(dp[N] % 1000000000)