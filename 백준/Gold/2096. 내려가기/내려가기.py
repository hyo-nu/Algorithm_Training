import sys
input = sys.stdin.readline

N, INF = int(input()), int(1e9)
max_dp = [[0] * 3 for _ in range(2)]
min_dp = [[0] * 3, [INF] * 3]

for _ in range(N):
    nums = list(map(int, input().split()))

    for i in range(3):
        if i != 0 : max_dp[1][i - 1] = max(max_dp[1][i - 1], max_dp[0][i] + nums[i - 1])
        if i != 2 : max_dp[1][i + 1] = max(max_dp[1][i + 1], max_dp[0][i] + nums[i + 1])
        max_dp[1][i] = max(max_dp[1][i], max_dp[0][i] + nums[i])

        if i != 0 : min_dp[1][i - 1] = min(min_dp[1][i - 1], min_dp[0][i] + nums[i - 1])
        if i != 2 : min_dp[1][i + 1] = min(min_dp[1][i + 1], min_dp[0][i] + nums[i + 1])
        min_dp[1][i] = min(min_dp[1][i], min_dp[0][i] + nums[i])

    max_dp[0], max_dp[1] = max_dp[1], max_dp[0]
    min_dp[0], min_dp[1] = min_dp[1], [INF] * 3

print(max(max_dp[0]),min(min_dp[0]))