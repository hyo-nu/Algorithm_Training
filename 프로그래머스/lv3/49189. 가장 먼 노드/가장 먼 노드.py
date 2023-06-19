from collections import deque

def solution(n, edge):
    G = [[] for _ in range(n+1)]
    vi = [0] * (n + 1)
    for u, v in edge:
        G[u].append(v)
        G[v].append(u)
        
    vi[0] = -1
    vi[1] = 1
    Q = deque()
    Q.append(1)
    move = 2
    while 0 in vi:        
        def BFS(move):
            tmp = []
            while Q:
                v = Q.popleft()
                for w in G[v]:
                    if not vi[w]:
                        vi[w] = move
                        tmp.append(w)
            return tmp
        Q.extend(BFS(move))
        move += 1
    
    return vi.count(max(vi))