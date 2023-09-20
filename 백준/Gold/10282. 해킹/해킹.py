import sys
input = sys.stdin.readline
from heapq import heappop,heappush

INF = int(1e9)
Test = int(input())

for _ in range(Test):
    n, d, c = map(int,input().split())

    G = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int,input().split())
        G[b].append((a,s))

    h = []
    heappush(h,(0,c))
    Distance = [INF] * (n + 1)
    Distance[c] = 0

    while h:
        distance_start, start = heappop(h)
        if Distance[start] < distance_start : continue

        for next, weight in G[start]:
            if Distance[next] > Distance[start] + weight:
                Distance[next] = Distance[start] + weight
                heappush(h,(Distance[start] + weight,next))

    count = EndSecond = 0
    for i in range(1,n + 1):
        if Distance[i] != INF :
            count += 1
            if EndSecond < Distance[i]:
                EndSecond = Distance[i]

    print(count,EndSecond)