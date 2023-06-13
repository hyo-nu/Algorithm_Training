def DFS(SP,EP):
    S = [SP]
    vi = [0] * (N + 1)
    vi[SP] = 1
    move = []

    while S:
        for NP,D in G[SP]:
            if not vi[NP]:
                S.append(SP)
                vi[NP] = 1
                SP = NP
                move.append(D)
                break
        else:
            SP = S.pop()
            move.pop()
        if SP == EP:
            return move

N, M = map(int,input().split())
G = [[] for _ in range(N+1)]

# 간선 입력 및 표시
for _ in range(N-1):
    u,v,d = map(int,input().split())
    G[u].append((v,d))
    G[v].append((u,d))

for _ in range(M):
    SP,EP = map(int,input().split())
    move = DFS(SP,EP)
    print(sum(move))