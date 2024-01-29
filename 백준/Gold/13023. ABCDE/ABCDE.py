import sys
input = sys.stdin.readline

def DFS(n):
    global result, cnt
    if cnt == 5 :
        result = 1
        return
    for np in G[n]:
        if not vi[np]:
            vi[np] = 1
            cnt += 1
            DFS(np)
            cnt -= 1
            vi[np] = 0


N, M = map(int,input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

for n in range(N):
    vi = [0] * N
    vi[n] = cnt = 1
    result = 0
    DFS(n)
    if result : break

print(result)