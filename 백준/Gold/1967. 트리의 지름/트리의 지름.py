from collections import deque

def BFS(sp):
    Q = deque([sp])
    vi = [-1] * (Node + 1)
    vi[sp] = long = ep = 0
    while Q:
        sp = Q.popleft()
        for np, weight in G[sp]:
            if vi[np] == -1:
                vi[np] = vi[sp] + weight
                Q.append(np)
                if long < vi[np]:
                    long = vi[np]
                    ep = np
    return long, ep

Node = int(input())
G = [[] for _ in range(Node+1)]

for _ in range(Node-1):
    u, v, weight = map(int,input().split())
    G[u].append((v,weight))
    G[v].append((u,weight))

start = 1
tmp, end = BFS(start)
diameter, tmp = BFS(end)
print(diameter)