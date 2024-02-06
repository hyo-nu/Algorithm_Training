import sys;
input = sys.stdin.readline

N, K = map(int,input().split())
nums = list(map(int,input().split()))

cnt = nums.count(K)
for i in range(2, N + 1):
    sp = 0
    ep = i
    value = sum(nums[:i])
    while ep < N :
        if value == K : cnt += 1
        value = value - nums[sp] + nums[ep]
        sp += 1 ; ep += 1
    if value == K : cnt += 1

print(cnt)