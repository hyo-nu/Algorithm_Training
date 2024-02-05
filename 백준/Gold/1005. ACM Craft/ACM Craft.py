import sys;
from collections import deque
input = sys.stdin.readline

def Topology_sort():
    Q = deque()
    for i in range(1,N + 1):
        if indegree[i] == 0 :
            Q.append((i, Ds[i]))

    while Q:
        sp, time = Q.popleft()
        for ep, weight in G[sp]:
            indegree[ep] -= 1
            Ds[ep] = max(Ds[ep], time + weight)
            if indegree[ep] == 0:
                Q.append((ep,Ds[ep])
                         )
for test in range(int(input())):
    N, K = map(int,input().split())
    Ds = [0] + list(map(int,input().split()))
    G = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)

    for _ in range(K):
        sp, ep = map(int,input().split())
        indegree[ep] += 1
        G[sp].append((ep,Ds[ep]))

    target = int(input())
    Topology_sort()
    print(Ds[target])