import sys;
from collections import deque
input = sys.stdin.readline


def Topology_sort():
    Q = deque()
    routes = []

    for i in range(1, N + 1):
        if indegree[i] == 0:
            Q.append(i)
            routes.append(i)

    while Q:
        sp = Q.popleft()
        for ep in G[sp]:
            indegree[ep] -= 1
            if indegree[ep] == 0:
                Q.append(ep)
                routes.append(ep)

    return routes

N, M = map(int, input().split())
indegree = [0] * (N + 1)
G = [[] for _ in range(N + 1)]

for _ in range(M):
    cnt, *singers = map(int, input().split())
    for i in range(1, cnt):
        sp, ep = singers[i-1], singers[i]
        indegree[ep] += 1
        G[sp].append(ep)

routes = Topology_sort()
if len(routes) == N:
    for route in routes:
        print(route)
else : print(0)