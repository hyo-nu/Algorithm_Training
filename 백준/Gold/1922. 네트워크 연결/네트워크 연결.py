import sys
input = sys.stdin.readline

def find_parent(sp):
    if sp != parent[sp]:
        parent[sp] = find_parent(parent[sp])
    return parent[sp]

def union(sp,ep):
    parent[find_parent(sp)] = find_parent(ep)

N, M = int(input()), int(input())

G = []
for _ in range(M):
    u, v, weight = map(int,input().split())
    G.append((u, v, weight))

parent = [i for i in range(N + 1)]
G.sort(key = lambda x : x[2])

Min = edge = 0
for sp, ep, weight in G:
    if find_parent(sp) != find_parent(ep):
        Min += weight
        edge += 1
        union(sp,ep)
        if edge == N - 1:
            break
print(Min)