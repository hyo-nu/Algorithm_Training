import sys;
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]

for r in range(n-1,-1,-1):
    for c in range(r, n):
        if c - r < 3:
            if nums[r] == nums[c] : dp[r][c] = 1
            else : dp[r][c] = 0
        else:
            if dp[r+1][c-1] and nums[r] == nums[c] : dp[r][c] = 1
            else : dp[r][c] = 0

for _ in range(int(input())):
    start, end = map(int, input().split())
    print(dp[start-1][end-1])