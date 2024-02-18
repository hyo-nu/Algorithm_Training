import sys;
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def find(sp):
    if sp != parents[sp]:
        parents[sp] = find(parents[sp])
    return parents[sp]

def union(sp,ep):
    parents[find(sp)] = find(ep)

while True:
    m,n = map(int,input().split())
    if m == 0 and n == 0 : break

    parents = list(range(m + 1))
    G = []
    total_price = 0
    for _ in range(n):
        sp, ep, weight = map(int,input().split())
        G.append((sp,ep,weight))
        total_price += weight

    G.sort(key=lambda x : x[2])

    Min = edge = 0
    for sp, ep, weight in G:
        if find(sp) != find(ep):
            union(sp,ep)
            Min += weight
            edge += 1
            if edge == m - 1:
                break

    print(total_price - Min)