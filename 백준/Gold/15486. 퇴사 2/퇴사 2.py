import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)

for i in range(1, N+1):
    day, money = map(int,input().split())
    dp[i] = max(dp[i], dp[i-1])
    if i + day <= N + 1:
        dp[i + day -1] = max(dp[i + day -1], dp[i-1] + money)

print(dp[N])