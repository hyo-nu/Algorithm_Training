import sys;
input = sys.stdin.readline

def find(sp):
    if sp != parents[sp]:
        parents[sp] = find(parents[sp])
    return parents[sp]

def union(sp, ep):
    parents[find(sp)] = find(ep)

N = int(input())
parents = [i for i in range(N + 1)]
star = [(i,*list(map(float,input().split()))) for i in range(1, N + 1)]
G = []
for i in range(N-1):
    for j in range(i+1,N):
        distance = ((star[i][1] - star[j][1]) ** 2 + (star[i][2] - star[j][2]) ** 2) ** (1/2)
        G.append((star[i][0], star[j][0], round(distance,2)))

G.sort(key = lambda x:x[2])

Min = edge = 0
for sp, ep, distance in G:
    if find(sp) != find(ep):
        Min += distance
        edge += 1
        union(sp, ep)
        if edge == N-1:
            break
print(Min)