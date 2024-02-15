import sys;
input = sys.stdin.readline

INF = int(1e9)
n, m = int(input()), int(input())
G = [[INF] * n for _ in range(n)]
route = [[0] * n for _ in range(n)]

for _ in range(m):
    sp, ep, weight = map(int,input().split())
    if G[sp-1][ep-1] > weight:
        G[sp-1][ep-1] = weight
        route[sp-1][ep-1] = ep

for k in range(n):
    for r in range(n):
        for c in range(n):
            if r == c : G[r][c] = 0
            if G[r][c] > G[r][k] + G[k][c]:
                # print(k+1,r+1,c+1,"=>",G[r][c],":",G[r][k],"+",G[k][c],"=",G[r][k] + G[k][c])
                G[r][c] = G[r][k] + G[k][c]
                # for lst in route:print(lst)
                # print("=")
                if route[k][c] == c + 1 :
                    route[r][c] = k + 1
                else :
                    route[r][c] = route[k][c]
                # for lst in route:print(lst)
                # print("=============")

# for lst in route : print(lst)
# print("=====")
for r in range(n):
    for c in range(n):
        if G[r][c] == INF : G[r][c] = 0
            
for lst in G:print(*lst)
for r in range(n):
    for c in range(n):
        if not route[r][c] : print(0) ; continue
        dc = c
        move = [c + 1]
        while route[r][dc] != dc + 1:
            move.append(route[r][dc])
            dc = route[r][dc] - 1
        move.append(r + 1)
        print(len(move),*move[::-1])
        # print(r,c,"=>",len(move),*move[::-1])