import sys;
from collections import deque
input = sys.stdin.readline

def Topology_sort():
    Q = deque()
    Min = 0

    for i in range(1, N + 1):
        if not indegree[i]:
            Min = max(Min, worktime[i])
            Q.append((i,worktime[i]))

    while Q:
        sp, time = Q.popleft()
        for ep, weight in G[sp]:
            indegree[ep] -= 1
            Min = max(Min, time + weight)
            worktime[ep] = max(worktime[ep],time + weight)
            if not indegree[ep]:
                Q.append((ep, worktime[ep]))
    return Min

N = int(input())
indegree = [0] * (N + 1)
worktime = [0] * (N + 1)
G = [[] for _ in range(N + 1)]

for ep in range(1, N + 1):
    weight, cnt, *sp_lst = map(int,input().split())
    worktime[ep] = weight
    if cnt > 0 :
        for sp in sp_lst:
            indegree[ep] += 1
            G[sp].append((ep,weight))

print(Topology_sort())