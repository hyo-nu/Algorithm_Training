from collections import deque

def BFS(sp):
    Q = deque()
    Q.append(sp)
    vi = [-1] * (N + 1)
    vi[sp] = longest = longest_point = 0
    while Q:
        sp = Q.popleft()
        for np, w in G[sp]:
            if vi[np] == -1:
                vi[np] = vi[sp] + w
                Q.append(np)
                if longest < vi[np]:
                    longest = vi[np]
                    longest_point = np
    return longest, longest_point

N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    sp, ep, w = map(int,input().split())
    G[sp].append((ep,w))
    G[ep].append((sp,w))

start = 1
tmp1, end = BFS(start)
diameter, tmp2 = BFS(end)
print(diameter)