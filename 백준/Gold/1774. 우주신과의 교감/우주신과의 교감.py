import sys;
input = sys.stdin.readline

def find(sp):
    if parents[sp] != sp:
        parents[sp] = find(parents[sp])
    return parents[sp]

def union(sp,ep):
    parents[find(sp)] = find(ep)

n, m = map(int,input().split())
parents = list(range(n + 1))
G = []
god = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        weight = ((god[i][0]-god[j][0])**2 + (god[i][1]-god[j][1])**2) ** (1/2)
        G.append((i+1,j+1,weight))

G.sort(key=lambda x:x[2])

edge = 0
for _ in range(m):
    sp,ep = map(int,input().split())
    if find(sp) != find(ep):
        union(sp,ep)
        edge += 1

Min = 0
for sp,ep,weight in G:
    if find(sp) != find(ep):
        Min += weight
        edge += 1
        union(sp,ep)
        if edge == n-1:
            break

print(format(Min,".2f"))