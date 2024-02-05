import sys;
input = sys.stdin.readline

def find(sp):
    if sp != parents[sp]:
        parents[sp] = find(parents[sp])
    return parents[sp]

def union(sp, ep):
    parents[find(sp)] = find(ep)

N, M = int(input()), int(input())
G = [list(map(int, input().split())) for _ in range(N)]
routes = list(map(int, input().split()))
parents = [i for i in range(N + 1)]

for r in range(N):
    for c in range(r + 1, N):
        if G[r][c] == 1 : union(r+1,c+1)

for i in range(1, len(routes)):
    if find(routes[i]) != find(routes[i-1]):
        print("NO")
        break
else:
    print("YES")