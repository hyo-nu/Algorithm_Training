import sys;
input = sys.stdin.readline

def find(sp):
    if sp != parents[sp]:
        parents[sp] = find(parents[sp])
    return parents[sp]

def union(sp,ep):
    parents[find(sp)] = find(ep)

n, m, k = map(int, input().split())
prices = list(map(int,input().split()))
parents = list(range(n + 1))
friends = [0] * (n+1)

for _ in range(m):
    sp, ep = map(int,input().split())
    union(sp,ep)

for sp in range(1, n + 1):
    ep = find(sp)
    if friends[ep] == 0 :  friends[ep] = prices[sp-1] ; continue
    friends[ep] = min(friends[ep], prices[sp-1])

friends_fee = sum(friends)
print(friends_fee if friends_fee <= k else "Oh no")