import sys;
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def find(sp):
    if sp != parents[sp]:
        parents[sp] = find(parents[sp])
    return parents[sp]

def union(sp, ep):
    parents[find(sp)] = find(ep)

n, m = map(int,input().split())
parents = list(range(n))
for order in range(1,m + 1):
    sp, ep = map(int,input().split())
    if find(sp) == find(ep):
        print(order)
        break
    else :
        union(sp, ep)
else:
    print(0)