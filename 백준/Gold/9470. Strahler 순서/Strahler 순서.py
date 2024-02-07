import sys;
from collections import deque
input = sys.stdin.readline

def Topology():
    Q = deque()

    for i in range(1, M + 1):
        if indegree[i] == 0:
            Q.append(i)
            lst[i] = 1
            Strahler[i][1] = 1

    while Q:
        sp = Q.popleft()
        for ep in G[sp]:
            indegree[ep] -= 1
            Strahler[ep][lst[sp]] = Strahler[ep].get(lst[sp], 0) + 1
            if indegree[ep] == 0:
                Q.append(ep)
                tmp = sorted(Strahler[ep].items(),key = lambda x : (-x[1],-x[0]))
                if tmp[0][1] < 2:
                    lst[ep] = tmp[0][0]
                else :
                    lst[ep] = tmp[0][0] + 1
for _ in range(int(input())):
    K, M, P  = map(int, input().split())
    indegree = [0] * (M + 1)
    lst = [0] * (M + 1)
    Strahler = [{} for _ in range(M + 1)]
    G = [[] for _ in range(M + 1)]
    for _ in range(P):
        A, B = map(int, input().split())
        indegree[B] += 1
        G[A].append(B)

    Topology()
    print(K, max(lst))