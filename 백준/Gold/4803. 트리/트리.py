import sys;
input = sys.stdin.readline

def find(sp):
    if sp != parents[sp]:
        parents[sp] = find(parents[sp])
    return parents[sp]

def union(sp,ep):
    parents[find(sp)] = find(ep)

case = 1
while True:
    n, m = map(int,input().split())
    parents = list(range(n + 1))
    tree = [0] * (n + 1)
    if n == 0 and m == 0: break

    cycle = set()
    for _ in range(m):
        sp, ep = map(int,input().split())
        if find(sp) == find(ep) :
            tree[parents[sp]] = -1
        elif tree[find(sp)] == -1 or tree[find(ep)] == -1:
            tree[find(sp)] = tree[find(ep)] = -1
        union(sp,ep)

    count = 0
    for sp in range(1, n + 1):
        ep = find(sp)
        if tree[ep] != -1 and tree[ep] == 0:
            tree[ep] = 1
            count += 1

    if count > 1 :
        print(f'Case {case}: A forest of {count} trees.')
    elif count == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: No trees.')
    case += 1