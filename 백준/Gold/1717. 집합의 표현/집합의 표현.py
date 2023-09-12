import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def find_parent(sp):
    if sp != parent[sp]:
	    parent[sp] = find_parent(parent[sp])
    return parent[sp]

def union(sp,ep):
    parent[find_parent(sp)] = find_parent(ep)

N, M = map(int,input().split())
parent = [i for i in range(N + 1)]

for _ in range(M):
    Type, a, b = map(int,input().split())
    if not Type:
        union(a,b)
    elif Type:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")