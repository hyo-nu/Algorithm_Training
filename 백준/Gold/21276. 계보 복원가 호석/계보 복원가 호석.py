import sys;
input = sys.stdin.readline
from collections import deque

N = int(input())
name_dict = {}
name_dict_re = {}
pedigree = {}
family = sorted(list(map(str,input().split())))

for idx, name in enumerate(family):
    name_dict[name] = idx
    name_dict_re[idx] = name
    pedigree[name] = []

indegree = [0] * N
G = [[] for _ in range(N)]
for _ in range(int(input())):
    child, parent = map(str, input().split())
    c, p = name_dict[child], name_dict[parent]
    G[p].append(c)
    indegree[c] += 1

def Topology_sort():
    global root_parents
    root_parents = []
    Q = deque()

    for i in range(N):
        if indegree[i] == 0:
            Q.append((i,0))
            root_parents.append(name_dict_re[i])

    while Q:
        now, order = Q.popleft()

        for g in G[now]:
            indegree[g] -= 1
            if indegree[g] == 0:
                Q.append((g,order+1))
                pedigree[name_dict_re[now]].append(name_dict_re[g])

Topology_sort()
print(len(root_parents))
print(*root_parents)

for name in family:
    print(name, len(pedigree[name]), *pedigree[name])