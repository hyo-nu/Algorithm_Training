import sys
input = sys.stdin.readline

N = int(input())
max_dp = [[0] * 5 for _ in range(2)]
min_dp = [[0] * 5, [int(1e9)] * 5]

for _ in range(N):
    nums = list(map(int, input().split()))
    max_nums = [0] + nums + [0]
    min_nums = [int(1e9)] + nums + [int(1e9)]

    for i in range(1, 4) :
        max_dp[1][i - 1] = max(max_dp[1][i - 1], max_dp[0][i] + max_nums[i - 1])
        max_dp[1][i] = max(max_dp[1][i], max_dp[0][i] + max_nums[i])
        max_dp[1][i + 1] = max(max_dp[1][i + 1], max_dp[0][i] + max_nums[i + 1])

        min_dp[1][i-1] = min(min_dp[1][i-1], min_dp[0][i] + min_nums[i-1])
        min_dp[1][i] = min(min_dp[1][i], min_dp[0][i] + min_nums[i])
        min_dp[1][i+1] = min(min_dp[1][i+1], min_dp[0][i] + min_nums[i+1])

    max_dp[0], max_dp[1] = max_dp[1], max_dp[0]
    min_dp[0], min_dp[1] = min_dp[1], [int(1e9)] * 5

print(max(max_dp[0][1:-1]),min(min_dp[0][1:-1]))