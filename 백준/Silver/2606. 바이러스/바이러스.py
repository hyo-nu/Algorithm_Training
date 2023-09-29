import sys
input = sys.stdin.readline
from collections import deque

N, M = int(input()), int(input())

G = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

Q = deque([1])
vi = [0] * (N + 1)
vi[1] = 1

virus = 0
while Q:
    now = Q.popleft()
    for next in G[now]:
        if not vi[next]:
            Q.append(next)
            vi[next] = 1
            virus += 1

print(virus)