import sys;
input = sys.stdin.readline

def find(sp,parents):
    if parents[sp] != sp:
        parents[sp] = find(parents[sp],parents)
    return parents[sp]

def union(sp,ep,parents):
    parents[find(sp,parents)] = find(ep,parents)

def MST(Min, edge, parents):
    for sp, ep, road in G:
        if find(sp,parents) != find(ep,parents):
            if road == 0 : Min += 1
            edge += 1
            union(sp, ep,parents)
            if edge == n:
                break
    return Min

n, m = map(int,input().split())
parents1 = list(range(n + 1))
parents2 = list(range(n + 1))
Min, edge = 0, 1
G = []

for i in range(m + 1):
    sp, ep, road = map(int,input().split())
    if i == 0 :
        union(sp,ep,parents1)
        union(sp,ep,parents2)
        if road == 0 : Min += 1
    else:G.append((sp, ep, road))

G.sort(key = lambda x : -x[2])
best = MST(Min, edge, parents1)
G.sort(key = lambda x : x[2])
worst = MST(Min, edge, parents2)

print(worst**2 - best**2)