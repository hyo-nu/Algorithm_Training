import sys
input = sys.stdin.readline

str1, str2, str3 = input().rstrip(),input().rstrip(),input().rstrip()
R, C, K = len(str1),len(str2),len(str3)
dp = [[[0] * (C+1) for _ in range(R+1)] for _ in range(K+1)]

for k in range(1, K + 1):
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if str1[r-1] == str2[c-1] == str3[k-1]:
                dp[k][r][c] = dp[k-1][r-1][c-1] + 1
            else:
                dp[k][r][c] = max(
                    dp[k-1][r][c],
                    dp[k][r-1][c],
                    dp[k][r][c-1],)

print(dp[-1][-1][-1])