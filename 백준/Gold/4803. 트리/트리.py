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
    if n == 0 and m == 0: break

    cycle = set()
    for _ in range(m):
        sp, ep = map(int,input().split())
        if find(sp) == find(ep) :
            cycle.add(parents[sp]) ;
        elif parents[sp] in cycle or parents[ep] in cycle:
            cycle.add(parents[sp]) ; cycle.add(parents[ep])

        union(sp,ep)

    for sp in range(1, n + 1):
        find(sp)
    parents = set(parents)
    count = sum([1 if i not in cycle else 0 for i in parents]) - 1
    if count > 1 :
        print(f'Case {case}: A forest of {count} trees.')
    elif count == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: No trees.')
    case += 1