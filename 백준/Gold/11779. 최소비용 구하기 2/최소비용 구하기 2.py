import sys
input = sys.stdin.readline

from heapq import heappop, heappush

INF = int(1e9)
n, m = int(input()), int(input())
G = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, weight = map(int,input().split())
    G[u].append([v, weight])

start, arrive = map(int,input().split())

h = []
heappush(h,(0,start))
Distance = [[INF,[]] for _ in range(n + 1)]
Distance[start][0] = 0
Distance[start][1].append(start)

while h:
    start_distance, start = heappop(h)
    if Distance[start][0] < start_distance : continue

    for next, weight in G[start]:
        if Distance[next][0] > Distance[start][0] + weight:
            Distance[next][0] = Distance[start][0] + weight
            Distance[next][1] = Distance[start][1] + [next]
            heappush(h,(Distance[start][0] + weight, next))

print(Distance[arrive][0])
print(len(Distance[arrive][1]))
print(*Distance[arrive][1])