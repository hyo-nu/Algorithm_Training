import sys
input = sys.stdin.readline

def find(sp):
    if sp == rep[sp]:
        return sp
    rep[sp] = find(rep[sp])
    return rep[sp]

def union(sp,ep):
    rep[find(sp)] = find(ep)

V, E = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(E)]
G.sort(key=lambda x:x[2])
rep = [i for i in range(V + 1)]

Min = edge = 0
for sp, ep, weight in G:
    if find(sp) != find(ep):
        Min += weight
        edge += 1
        union(sp,ep)
        if edge == V-1:
            break
print(Min)