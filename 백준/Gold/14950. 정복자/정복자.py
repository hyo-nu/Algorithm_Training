import sys;
input = sys.stdin.readline

def find(sp):
    if parents[sp] != sp:
        parents[sp] = find(parents[sp])
    return parents[sp]

def union(sp, ep):
    parents[find(sp)] = find(ep)

n, m, t = map(int, input().split())
parents = list(range(n+1))
G = []
for _ in range(m):
    sp, ep, weight = map(int,input().split())
    G.append((sp, ep, weight))

G.sort(key=lambda x:x[2])

Min = edge = 0
for sp, ep, weight in G:
    if find(sp) != find(ep):
        Min += (weight + edge*t)
        edge += 1
        union(sp, ep)
        if edge == n-1:
            break

print(Min)