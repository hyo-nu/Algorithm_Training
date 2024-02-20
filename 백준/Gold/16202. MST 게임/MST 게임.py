import sys;
input = sys.stdin.readline

def find(sp):
    if parents[sp] != sp:
        parents[sp] = find(parents[sp])
    return parents[sp]

def union(sp, ep):
    parents[find(sp)] = find(ep)

n, m, k = map(int, input().split())
G = []
for weight in range(1, m + 1):
    sp, ep = map(int,input().split())
    G.append((sp, ep, weight))

result = []
for i in range(k):
    Min = edge = 0
    parents = list(range(n + 1))
    for sp, ep, weight in G[i:]:
        if find(sp) != find(ep):
            Min += weight
            edge += 1
            union(sp, ep)
            if edge == n-1:
                break
    result.append(Min if edge == n-1 else 0)
print(*result)