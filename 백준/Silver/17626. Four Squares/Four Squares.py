import math

n = int(input())
dp = [50001] * (n+1)
dp[0] = 0
for i in range(1,n+1):
    if i % (i**(0.5)) == 0 : dp[i] = 1
    for j in range(1, math.floor(i ** (0.5))+1):
        dp[i] = min(dp[i-( j ** 2)] + 1,dp[i])

print(dp[n])