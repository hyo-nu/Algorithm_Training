N = int(input())
lst = [0] + list(map(int,input().split()))
dp = [0] * (N + 1)
dp[1] = lst[1]
for i in range(2,N+1):
    for j in range(i+1):
        dp[i] = max(dp[i],dp[j]+lst[i-j])
print(dp[N])