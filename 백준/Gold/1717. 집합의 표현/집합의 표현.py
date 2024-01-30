import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def find_parent(sp):
    if sp != parent[sp]:
        parent[sp] = find_parent(parent[sp])
    return parent[sp]

def union(sp, ep):
    parent[find_parent(sp)] = find_parent(ep)

N, M = map(int,input().split())
parent = [i for i in range(N + 1)]

for _ in range(M):
    act, sp, ep = map(int,input().split())
    if not act :
        union(sp, ep)
    else :
        if find_parent(sp) == find_parent(ep) : print("YES")
        else : print("NO")