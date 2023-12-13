import sys
input = sys.stdin.readline
from itertools import combinations

INF = 1e9
N, M = map(int,input().split())
houses, chickens = [], []

for r in range(N):
    tmp = list(map(int,input().split()))
    for c in range(N):
        if tmp[c] == 1 : houses.append((r,c))
        elif tmp[c] == 2 : chickens.append((r,c))

H, C = len(houses), len(chickens)
G = [[0] * H for _ in range(C)]

for r in range(C):
    for c in range(H):
        G[r][c] = abs(houses[c][0] - chickens[r][0]) + abs(houses[c][1] - chickens[r][1])

Min_distance = INF
for choices in combinations(range(C), M):
    new_G = list(zip(*list(G[choice] for choice in choices)))
    distance = sum(min(new_G[r]) for r in range(H))
    Min_distance = min(Min_distance, distance)
print(Min_distance)

