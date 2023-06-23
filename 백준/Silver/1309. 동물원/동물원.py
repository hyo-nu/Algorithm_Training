N = int(input())
dp = [1,1,1]
for _ in range(N-1):
    for i in range(3):
        if i == 0 : dp[i] = sum(dp)
        else: dp[i] = dp[0] - dp[i]
            
print(sum(dp) % 9901)