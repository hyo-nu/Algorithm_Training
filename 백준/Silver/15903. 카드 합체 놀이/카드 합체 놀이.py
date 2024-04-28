from heapq import heappop, heappush, heapify

n, m = map(int,input().split())
nums = list(map(int,input().split()))
heapify(nums)
for _ in range(m):
    one, two = heappop(nums), heappop(nums)
    heappush(nums, one + two)
    heappush(nums, one + two)

print(sum(nums))
