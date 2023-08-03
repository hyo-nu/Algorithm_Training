from collections import deque
import sys;
input = sys.stdin.readline

N, M, K, X = map(int,input().split())
G = [[] for _ in range(N+1)]
vi = [-1] * (N+1)

for _ in range(M):
    u, v = map(int,input().split())
    G[u].append(v)

Q = deque([X])
vi[X] = 0

while Q:
    SP = Q.popleft()
    for NP in G[SP]:
        if vi[NP] == -1:
            Q.append(NP)
            vi[NP] = vi[SP] + 1

flag = 0
for i in range(len(vi)):
    if vi[i] == K:
        flag += 1
        print(i)
if not flag : print(-1)