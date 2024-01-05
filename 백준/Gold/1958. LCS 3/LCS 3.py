import sys
input = sys.stdin.readline

str1, str2, str3 = input().rstrip(),input().rstrip(),input().rstrip()
R, C, K = len(str1),len(str2),len(str3)
dp = [[[0] * (R+1) for _ in range(C+1)] for _ in range(K+1)]

for k in range(1, K + 1):
    for c in range(1, C + 1):
        for r in range(1, R + 1):
            if str1[r-1] == str2[c-1] == str3[k-1]:
                dp[k][c][r] = dp[k-1][c-1][r-1] + 1
            else:
                dp[k][c][r] = max(
                    dp[k][c-1][r],
                    dp[k-1][c-1][r],
                    dp[k-1][c][r],
                    dp[k][c][r-1],
                    dp[k-1][c][r-1],
                    dp[k][c-1][r-1])

print(dp[K][C][R])