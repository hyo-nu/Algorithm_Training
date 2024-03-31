str1, str2 = input().rstrip(), input().rstrip()

R, C = len(str1), len(str2)
dp = [[0] * (C+1) for _ in range(R+1)]
for r in range(1,R + 1):
    for c in range(1,C + 1):
        if str1[r-1] == str2[c-1]:
            dp[r][c] = dp[r-1][c-1] + 1
        else :
            dp[r][c] = max(dp[r-1][c], dp[r][c-1])
print(dp[R][C])