import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0] * (N + 1)
G = [[] for _ in range(N + 1)]

for _ in range(M):
    sp, ep = map(int,input().split())
    indegree[ep] += 1
    G[sp].append(ep)

def Topology_sort():
    Q = deque()
    route = [0] * (N + 1)

    for i in range(1, N + 1):
        if indegree[i] == 0:
            route[i] = 1
            Q.append(i)

    while Q:
        sp = Q.popleft()

        for ep in G[sp]:
            indegree[ep] -= 1
            if indegree[ep] == 0:
                route[ep] = route[sp] + 1
                Q.append(ep)

    print(*route[1:])

Topology_sort()