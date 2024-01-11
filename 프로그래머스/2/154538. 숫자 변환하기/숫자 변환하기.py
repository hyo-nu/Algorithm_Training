def solution(x, y, n):
    
    dp = [y + 1] * (y + 1)
    dp[x] = 0
    
    for i in range(x, y + 1):
        if i - n >= x : dp[i] = min(dp[i], dp[i - n] + 1)
        if i // 2 >= x and i % 2 == 0: dp[i] = min(dp[i], dp[i // 2] + 1)
        if i // 3 >= x and i % 3 == 0: dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return dp[y] if dp[y] != y+1 else -1