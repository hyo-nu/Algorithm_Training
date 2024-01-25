import sys
from collections import deque
input = sys.stdin.readline

def BFS(sp) :
    Q = deque([sp])
    vi = [-1] * (node + 1)
    vi[sp] = long = ep = 0
    while Q:
        sp = Q.popleft()
        for np, weight in G[sp]:
            if vi[np] == -1 :
                Q.append(np)
                vi[np] = vi[sp] + weight
            if long < vi[np]:
                long = vi[np]
                ep = np
    return long, ep

node = int(input())
G = [[] for _ in range(node+1)]
for _ in range(node):
    num, *info, stop = map(int,input().split())

    for i in range(0,len(info),2):
        edge, weight = info[i:i+2]
        G[num].append((edge, weight))

start = 1
tmp, end = BFS(start)
result, tmp = BFS(end)
print(result)