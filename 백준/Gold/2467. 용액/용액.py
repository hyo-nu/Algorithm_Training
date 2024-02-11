import sys;
from collections import deque
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
sp, ep = 0, n-1
Min = 2000000001
result = []

while sp < ep :
    value = lst[sp] + lst[ep]

    if abs(value) < Min :
        Min = abs(value)
        result = [lst[sp],lst[ep]]

    if value <= 0 :
        sp += 1

    elif value > 0 :
        ep -= 1

print(*result)