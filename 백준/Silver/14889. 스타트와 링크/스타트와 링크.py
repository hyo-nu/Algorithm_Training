import sys
from itertools import combinations
input = sys.stdin.readline

def combi_cnt(total,choice):
    result = 1
    for i in range(total,choice,-1) : result *= i
    for i in range(1,choice + 1) : result /= i
    return int(result) // 2

N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]

Min = int(1e9)
case_cnt = combi_cnt(N, N//2)
for idx, start in enumerate(combinations(range(1, N + 1), N // 2),1):
    if idx > case_cnt : break
    start_cnt = rink_cnt = 0

    for r in start:
        for c in start:
            start_cnt += G[r-1][c-1]

    rink = [ i for i in range(1, N + 1) if i not in start ]

    for r in rink:
        for c in rink:
            rink_cnt += G[r-1][c-1]

    Min = min(Min, abs(start_cnt - rink_cnt))

print(Min)