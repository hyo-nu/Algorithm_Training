import sys
input = sys.stdin.readline

def find_parent(sp):
    if parent[sp] < 0:
        return sp
    ep = find_parent(parent[sp])
    parent[sp] = ep
    return ep

def union(sp, ep):
    parent[find_parent(sp)] = find_parent(ep)

N, M = map(int,input().split())
parent = [-1] * (N + 1)
G = []
cost = 0
for _ in range(M):
    a, b, c = map(int,input().split())
    G.append((a,b,c))
    cost += c

G.sort(key = lambda x : x[2])

Edge = Min = 0
for sp, ep, weight in G:
    if find_parent(sp) != find_parent(ep):
        Edge += 1
        Min += weight
        union(sp,ep)
        if Edge == N - 1:
            break

print( cost - Min if Edge == N -1 else -1)