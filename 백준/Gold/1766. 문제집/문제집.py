import sys;
from heapq import heappop, heappush
input = sys.stdin.readline

def Topology():
    h, route = [], []

    for i in range(1,n + 1):
        if indegree[i] == 0:
            heappush(h, i)

    while h:
        sp = heappop(h)
        route.append(sp)
        for ep in G[sp]:
            indegree[ep] -= 1
            if indegree[ep] == 0:
                heappush(h, ep)

    return route

n, m = map(int, input().split())
indegree = [0] * (n + 1)
G = [[] for _ in range(n + 1)]

for _ in range(m):
    sp, ep = map(int, input().split())
    indegree[ep] += 1
    G[sp].append(ep)

print(*Topology())