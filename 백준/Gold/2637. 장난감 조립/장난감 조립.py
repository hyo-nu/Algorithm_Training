import sys;
from collections import deque
input = sys.stdin.readline

def Topology():
    Q = deque()

    for i in range(1,N + 1):
        if indegree[i] == 0:
            Q.append(i)
            info[i][i] = 1

    while Q:
        sp = Q.popleft()
        for ep, cnt in G[sp]:
            indegree[ep] -= 1

            for key, value in info[sp].items():
                info[ep][key] = info[ep].get(key, 0) + (value * cnt)

            if indegree[ep] == 0:
                Q.append(ep)

N = int(input())
indegree = [0] * (N + 1)
G = [[] for _ in range(N + 1)]
info = [{} for _ in range(N + 1)]
for _ in range(int(input())):
    ep, sp, cnt = map(int, input().split())
    indegree[ep] += 1
    G[sp].append((ep,cnt))

Topology()
for lst in sorted(info[N].items()):
    print(*lst)