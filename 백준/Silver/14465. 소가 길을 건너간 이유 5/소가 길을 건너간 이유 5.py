import sys
from collections import deque
input = sys.stdin.readline

N, K, B = map(int,input().split())
road = [1] * (N + 1)
for _ in range(B) : road[int(input())] = 0

sp = ep = 1
prefix_sum = fixed = 0
fix_min = 100000

while ep <= N :
    if prefix_sum >= K:
        if road[ep] == 1 and road[sp] == 0:
            fixed -= 1

        elif road[ep] == 0 and road[sp] == 1:
            fixed += 1

        fix_min = min(fix_min, fixed)
        sp += 1 ; ep += 1

    elif road[ep] == 0 :
        fixed += 1
        prefix_sum += 1
        ep += 1

    elif road[ep] == 1 :
        prefix_sum += 1
        ep += 1

print(fix_min)