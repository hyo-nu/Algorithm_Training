import sys
input = sys.stdin.readline

def find_parent(sp):
    if sp != parent[sp]:
        parent[sp] = find_parent(parent[sp])
    return parent[sp]

def union(sp, ep):
    parent[find_parent(sp)] = find_parent(ep)

G, P = int(input()), int(input())

airs = [int(input()) for _ in range(P)]
parent = [i for i in range(G + 1)]

count = 0
for air in airs:
    if find_parent(air):
        union(parent[find_parent(air)],find_parent(air)-1)
        count += 1
    else : break

print(count)