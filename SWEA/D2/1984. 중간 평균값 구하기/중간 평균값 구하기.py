Test = int(input())

for T in range(Test):
    nums = list(map(int,input().split()))
    nums.sort()
    print(f'#{T+1} {round(sum(nums[1:9])/8)}')
