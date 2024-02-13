import sys;
input = sys.stdin.readline

def find(sp):
    if sp != parents[sp]:
        parents[sp] = find(parents[sp])
    return parents[sp]

def union(sp, ep):
    parents[find(sp)] = find(ep)

n = int(input())
star = [list(map(int,input().split()))+[i] for i in range(n)]
parents = list(range(n))
G = []

for xyz in range(3):
    star.sort(key = lambda x : x[xyz])

    for i in range(n-1):
        sp = star[i][3]
        ep = star[i + 1][3]
        weight = abs(star[i][xyz] - star[i + 1][xyz])
        G.append((sp, ep, weight))

G.sort(key = lambda x : x[2])

Min = edge = 0
for sp, ep, weight in G:
    if find(sp) != find(ep):
        Min += weight
        edge += 1
        union(sp, ep)
        if edge == n-1 : break

print(Min)