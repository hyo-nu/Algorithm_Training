import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def find(sp):
    if sp != parent[sp]:
        parent[sp] = find(parent[sp])
    return parent[sp]

def union(sp, ep):
    parent[find(sp)] = find(ep)

N = int(input())
parent = [i for i in range(N + 1)]
for _ in range(N-2):
    sp, ep = map(int,input().split())
    union(sp, ep)

answer = []
for i in range(1,N+1):
    if i == parent[i]:answer.append(i)

print(*answer)