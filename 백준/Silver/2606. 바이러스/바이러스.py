PC = int(input())
Edge = int(input())
G = [[] for _ in range(PC+1)]

for i in range(Edge):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

    SP = 1
    Q = []
    Q.append(SP)
    visited = [0] * (PC + 1)
    visited[SP] = 1

    while Q:
        NP = Q.pop(0)
        for w in G[NP]:
            if not visited[w]:
                visited[w] = 1
                Q.append(w)

print(visited.count(1)-1)