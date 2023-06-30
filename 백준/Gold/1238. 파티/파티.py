from collections import deque

N, M, T = map(int,input().split())
G = [[] for _ in range(N + 1)]

for _ in range(M):
    SP, EP, W = map(int,input().split())
    G[SP].append((EP,W))

def dijkstra(SP):
    Q = deque()
    Q.append(SP)
    D = [0xffffffff] * (N + 1)
    D[SP] = 0

    while Q:
        SP = Q.popleft()
        for NP, weight in G[SP]:
            if D[NP] > D[SP] + weight:
                D[NP] = D[SP] + weight
                Q.append(NP)
    return D

Back = dijkstra(T)
move_max = 0
for n in range(1,N+1):
    if n != T:
        Go = dijkstra(n)
        move_max = max(move_max,Go[T] + Back[n])
print(move_max)