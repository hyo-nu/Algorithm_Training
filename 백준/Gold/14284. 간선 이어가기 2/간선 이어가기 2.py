from collections import deque

V,E = map(int,input().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, weight = map(int,input().split())
    G[u].append((v,weight))
    G[v].append((u, weight))

SP, EP = map(int,input().split())
Q = deque()
Q.append(SP)
D = [0xffffffff] * (V + 1)
D[SP] = 0

while Q:
    v = Q.popleft()
    for w,weight in G[v]:
        if D[w] > D[v] + weight:
            D[w] = D[v] + weight
            Q.append(w)
print(D[EP])