from collections import deque

def BFS(FR,FC,SW):
    while h :
        t,r,c = heappop(h)
        for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
            nr,nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if vi[nr][nc] == -1 and G[nr][nc] <= SW:
                    heappush(h,(t+1,nr,nc))
                    vi[nr][nc] = vi[r][c] + 1
                    if vi[FR][FC] != -1 : return vi[FR][FC]
    return vi[FR][FC]

INF = int(1e9)

N = int(input())
G, Q = [], []
for r in range(N):
    tmp = list(map(int,input().split()))
    G.append(tmp)
    for c in range(N):
        if tmp[c] : Q.append((r,c,tmp[c]))

Q.sort(key = lambda x : x[2])
M = len(Q) - 1
SR, SC, SW = Q[M][0], Q[M][1], 2
G[SR][SC] = eat = total_distance = catch_fish = 0
catch = []

# print("시작이야")
# for lst in G:
#     print(lst)

while catch_fish <= M-1:
    vi = [[-1] * N for _ in range(N)]
    vi[SR][SC] = 0
    q = deque([(SR,SC)])
    Min_move = N ** 2 + 1
    mom = True

    while q :
        r, c = q.popleft()
        for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc <N:
                if G[nr][nc] <= SW and vi[nr][nc] == -1:
                    q.append((nr,nc))
                    vi[nr][nc] = vi[r][c] + 1

    for m in range(M):
        FR, FC, FW = Q[m]
        if FW >= SW: break
        elif FW < SW and m not in catch:
            if vi[FR][FC] != -1 and Min_move > vi[FR][FC]:
                TR, TC, fish, Min_move, mom = FR, FC, m, vi[FR][FC], False
            elif vi[FR][FC] != -1 and Min_move == vi[FR][FC]:
                if TR > FR:
                    TR, TC, fish, Min_move, mom = FR, FC, m, vi[FR][FC], False
                elif TR == FR and TC > FC:
                    TR, TC, fish, Min_move, mom = FR, FC, m, vi[FR][FC], False

    if mom: break
    G[TR][TC] = 0
    SR, SC = TR, TC
    total_distance += Min_move
    catch.append(fish)
    catch_fish += 1
    eat += 1

    if eat == SW:
        eat = 0
        SW += 1

    # print("===================")
    # print("TR:",TR)
    # print("TC:",TC)
    # print("이동:",Min_move)
    # for lst in G:
    #     print(lst)

print(total_distance)





