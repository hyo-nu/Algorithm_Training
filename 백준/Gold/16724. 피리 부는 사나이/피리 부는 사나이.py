import sys;
input = sys.stdin.readline

def find(sp):
    if sp != parents[sp]:
        parents[sp] = find(parents[sp])
    return parents[sp]

def union(sp, ep):
    parents[find(sp)] = find(ep)

n, m = map(int,input().split())
G = [list(input().rstrip()) for _ in range(n)]
parents = list(range(n * m))
sp = 0

for r in range(n):
    for c in range(m):
        if G[r][c] == "R" : ep = sp + 1
        elif G[r][c] == "D" : ep = sp + m
        elif G[r][c] == "L" : ep = sp - 1
        elif G[r][c] == "U" : ep = sp - m
        union(sp, ep)
        sp += 1

result = set()
for sp in range(n*m):
    result.add(find(sp))

print(len(result))