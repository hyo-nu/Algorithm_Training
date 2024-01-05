import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
Dict = Counter(nums)

print(round(sum(nums)/N))
print(sorted(nums)[N//2])

Max = 0
lst = []
for key, value in Dict.items():
    if Max < value :
        lst = [key]
        Max = value
    elif Max == value :
        lst.append(key)

lst.sort(key = lambda x:x)
print(lst[1] if len(lst) >=2 else lst[0])
print(sorted(nums)[-1]-sorted(nums)[0])