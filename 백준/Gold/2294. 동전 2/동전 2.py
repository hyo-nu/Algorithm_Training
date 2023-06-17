N, K = map(int,input().split())
dp = [0] + [100001] * K
coins = [int(input()) for _ in range(N)]

for money in range(K+2):
    for coin in coins:
        if money + coin <= K:
            dp[money + coin] = min(dp[money] + 1, dp[money + coin])

if dp[K] != 100001 : print(dp[K])
else: print(-1)
