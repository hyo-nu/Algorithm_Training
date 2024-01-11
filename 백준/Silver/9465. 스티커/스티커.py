import sys
input = sys.stdin.readline

for test in range(int(input())):
    n = int(input())
    stiker = [[0] + list(map(int,input().split())) for _ in range(2)]
    dp = [[0] * (n + 1) for _ in range(2)]
    dp[0][1] = stiker[0][1]
    dp[1][1] = stiker[1][1]

    for c in range(2,n+1):
        for r in range(2):
            dp[r][c] = max(dp[r][c], dp[0][c-2] + stiker[r][c], dp[1][c-2] + stiker[r][c])
            if r == 0 : dp[r][c] = max(dp[r][c], dp[1][c-1] + stiker[r][c])
            elif r == 1 : dp[r][c] = max(dp[r][c], dp[0][c-1] + stiker[r][c])

    print(max(dp[0][n],dp[1][n]))