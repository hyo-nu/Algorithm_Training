import sys
input = sys.stdin.readline

from heapq import heappop, heappush

INF = int(1e9)
n, m, r = map(int,input().split())
items = [0] + list(map(int,input().split()))
G = [[] for _ in range(n + 1)]

for _ in range(r):
    u, v, weight = map(int,input().split())
    G[u].append((v,weight))
    G[v].append((u,weight))

result = 0
for start in range(1,n + 1):
    h = []
    heappush(h,(0,start))
    Distance = [INF] * (n + 1)
    Distance[start] = 0
    score = 0

    while h:
        start_distance, start = heappop(h)
        if start_distance > Distance[start] : continue

        for next, weight in G[start] :
            if Distance[next] > Distance[start] + weight:
                Distance[next] = Distance[start] + weight
                heappush(h,(Distance[start] + weight, next))

    for spot in range(1,n + 1):
        if Distance[spot] <= m:
            score += items[spot]

    result = max(score,result)

print(result)