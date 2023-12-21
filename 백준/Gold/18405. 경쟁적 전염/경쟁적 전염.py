from collections import deque

def BFS():
    Q_tmp = []
    while Q:
        s, r, c = Q.popleft()
        for dr, dc in ((-1,0),(0,1),(1,0),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not G[nr][nc]:
                G[nr][nc] = s
                Q_tmp.append((s,nr,nc))
    return Q_tmp

N, K = map(int,input().split())
G, Q = [], []

for i in range(N):
    lst = list(map(int,input().split()))
    G.append(lst)
    for j in range(N):
        if lst[j] : Q.append((lst[j], i, j))

Q = deque(sorted(Q,key=lambda x:x[0]))
S, X, Y = map(int,input().split())

for _ in range(S):
    Q = deque(BFS())
print(G[X-1][Y-1])
