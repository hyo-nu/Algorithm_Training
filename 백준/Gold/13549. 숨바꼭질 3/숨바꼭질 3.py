from collections import deque

def BFS():
    while Q:
        XB = Q.popleft()
        if 0 <= XB * 2 <= 100000 and visited[XB * 2] == -1:
            Q.appendleft(XB * 2)
            visited[XB * 2] = visited[XB]
        for d in (-1,1):
            XA = XB + d
            if 0 <= XA <= 100000 and visited[XA] == -1:
                Q.append(XA)
                visited[XA] = visited[XB] + 1
            if XA == K :
                return

N, K = map(int,input().split())
Q = deque()
Q.append(N)
visited = [-1] * 100001
visited[N] = 0
BFS()
print(visited[K])