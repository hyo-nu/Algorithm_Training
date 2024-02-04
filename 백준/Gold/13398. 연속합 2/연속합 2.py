import sys;
input = sys.stdin.readline

N = int(input())
nums = [0] + list(map(int,input().split()))
dp1 = [0] * (N + 1)
dp2 = [0] * (N + 1)

if max(nums[1:]) < 0:
    Max = max(nums[1:])
else:
    for i in range(1, N + 1):
        dp1[i] = max(0, dp1[i-1] + nums[i])
        dp2[i] = max(0, dp2[i-1] + nums[i])
        if nums[i] < 0:
            dp2[i] = max(dp1[i-1], dp2[i])
    Max = max(max(dp1[1:]), max(dp2[1:]))

print(Max)