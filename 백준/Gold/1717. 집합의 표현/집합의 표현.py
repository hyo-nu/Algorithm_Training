import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def find(sp):
    if sp == rep[sp]:
        return sp

    rep[sp] = find(rep[sp])
    return rep[sp]

def union(sp,ep):
    sp = find(sp)
    ep = find(ep)

    if sp == ep:return

    if sp < ep:
        rep[ep] = sp
    else:
        rep[sp] = ep

N, M = map(int,input().split())
rep = [i for i in range(N + 1)]

for _ in range(M):
    flag, sp, ep = map(int,input().split())
    if flag :
        if find(sp) == find(ep) :
            print("YES")
        else :
            print("NO")
    else : union(sp, ep)
