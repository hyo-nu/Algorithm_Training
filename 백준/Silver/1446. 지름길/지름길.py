from heapq import heappop, heappush

# N : 지름길의 수
# D : 고속도로의 길이
# (시작위치, 도착위치, 지름길의 길이)

INF = int(1e9)
N, D = map(int,input().split())
G = [[] for _ in range(10001)]

for i in range(D):
    G[i].append((i+1, 1))

for n in range(N):
    sp, ep, weight = map(int,input().split())
    G[sp].append((ep, weight))

h = []
heappush(h,(0, 0))
Distance = [INF] * (10001)
Distance[0] = 0

while h:
    start_distance, start = heappop(h)
    if Distance[start] < start_distance : continue

    for next, weight in G[start]:
        if Distance[next] < Distance[start] + weight: continue
        Distance[next] = Distance[start] + weight
        heappush(h, (Distance[start] + weight, next))

print(Distance[D])
