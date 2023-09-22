import sys
input = sys.stdin.readline
from heapq import heappop, heappush

INF = int(1e9)
N, M = map(int,input().split())
G = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, weight = map(int,input().split())
    G[u].append((v,weight))
    G[v].append((u,weight))

h = []
start = 1
heappush(h,(0,start))
distances = [INF] * (N + 1)
distances[start] = 0

while h:
    start_distance, start = heappop(h)
    if distances[start] < start_distance: continue

    for next, weight in G[start]:
        if distances[next] > distances[start] + weight:
            distances[next] = distances[start] + weight
            heappush(h,(distances[start] + weight, next))

print(distances[N])