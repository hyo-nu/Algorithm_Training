from itertools import combinations

INF = 1e9
N, M = map(int,input().split())
houses, chickens = [], []

for r in range(N):
    tmp = list(map(int,input().split()))
    for c in range(N):
        if tmp[c] == 1 : houses.append((r,c))
        elif tmp[c] == 2 : chickens.append((r,c))

Min_distance = INF
for chicken in combinations(chickens, M):
    total_distance = 0
    for hr, hc in houses:
        distance = INF
        for cr, cc in chicken:
            distance = min(distance,abs(cr-hr) + abs(cc-hc))
        total_distance += distance
        if Min_distance <= total_distance:break
    Min_distance = min(total_distance,Min_distance)
print(Min_distance)