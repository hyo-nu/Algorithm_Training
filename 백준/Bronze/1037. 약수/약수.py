N = int(input())

nums = list(map(int,input().split()))
nums.sort()
num = nums[0]*nums[len(nums)-1]
print(num)