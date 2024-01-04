import sys

input = sys.stdin.readline
str1, str2 = input().rstrip(), input().rstrip()
R, C = len(str1), len(str2)
dp = [[0] * (C+1) for _ in range(R+1)]

for r in range(1,R + 1):
    for c in range(1,C + 1):
        if str1[r-1] == str2[c-1] : dp[r][c] = dp[r-1][c-1] + 1
        else : dp[r][c] = max(dp[r-1][c], dp[r][c-1])

LCS = ""
while R >= 1 and C >= 1:
    if str1[R-1] == str2[C-1]:
        LCS += str1[R-1]
        R -= 1 ; C -= 1
    else:
        if dp[R-1][C] > dp[R][C-1] : R -= 1
        else : C -= 1

print(len(LCS))
print(LCS[::-1])
