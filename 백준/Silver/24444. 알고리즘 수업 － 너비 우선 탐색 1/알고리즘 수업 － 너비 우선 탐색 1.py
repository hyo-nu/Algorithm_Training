import sys 
input = sys.stdin.readline

N,M,R = map(int,input().split())
G=[[] for _ in range(N + 1)]

for i in range(M):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

for i in G : i.sort()

visited = [0] * (N + 1)
visited[R] = 1
D = [0] * (N + 1)
D[R] = 1
Q = [R]
order = 2

while Q:
    V = Q.pop(0)
    for w in G[V]:
        if visited[w] == 0:
            visited[w] = 1
            Q.append(w)
            D[w] = order
            order += 1

for i in range(1,N+1):
    print(D[i])