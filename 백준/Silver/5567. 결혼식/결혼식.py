from collections import deque

N = int(input())
G = [[] for _ in range(N + 1)]
vi = [0] * (N + 1)

for _ in range(int(input())):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

Q = deque([1])
vi[1] = 1

while Q:
    now = Q.popleft()
    for next in G[now]:
        if not vi[next] :
            Q.append(next)
            vi[next] = vi[now] + 1

count = 0
for friend in vi[1:]:
    if friend >= 2 and friend <= 3:
        count += 1

print(count)