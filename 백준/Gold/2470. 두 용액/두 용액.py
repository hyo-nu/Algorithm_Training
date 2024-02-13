import sys;
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int,input().split())))

sp, ep = 0, n-1
liquids = []

Min = 2_000_000_000
while sp < ep:
    li1 = nums[sp]
    li2 = nums[ep]
    value = li1 + li2

    if Min > abs(value):
        Min = abs(value)
        liquids = [li1, li2]

    if value <= 0 :
        sp += 1

    elif value > 0 :
        ep -= 1

print(*liquids)