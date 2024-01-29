import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
INF = int(1e9)
G = [[INF] * (N + 1) for _ in range(N + 1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1 : break
    G[a][b] = G[b][a] = 1

for k in range(1 , N + 1):
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if r == c : G[r][c] = 0
            G[r][c] = min(G[r][c], G[r][k] + G[k][c])

people = []
Min = 100
for i in range(1,N + 1):
    cnt = max(G[i][1:])
    if Min > cnt :
        Min = cnt
        people = [i]
    elif Min == cnt:
        people.append(i)

print(Min,len(people))
print(*people)