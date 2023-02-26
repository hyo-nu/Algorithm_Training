from collections import deque

def Multi_BFS(Q,unripe):
    dr = [-1, 1, 0, 0, 0, 0] # 상,하
    dc = [ 0, 0,-1, 1, 0, 0] # 좌,우
    dh = [ 0, 0, 0, 0, 1,-1] # 위,아래
    day = 0
    if not unripe : return 0  # 덜익토가 없는 상태, 즉! 다 익음
    while Q:
        r,c,h = Q.popleft()
        for d in range(6):
            nr, nc, nh = r + dr[d], c + dc[d],h + dh[d]
            if 0 <= nr < N and 0<= nc < M and 0<= nh < H and box[nh][nr][nc] == -1:
                box[nh][nr][nc] = box[h][r][c] + 1
                Q.append((nr,nc,nh))
                if day < box[nh][nr][nc]:
                    day = box[nh][nr][nc]
    #덜익토 있는 경우 판단
    Sum = 0
    for arr in box:
        for lst in arr:
            Sum += lst.count(-1)
    if Sum : return -1
    else : return day

# M : 가로 , N : 세로
M, N, H = map(int,input().split())

Q = deque()
unripe = 0
box = []

for h in range(H):
    tomato = []
    for r in range(N):
        lst = list(map(int,input().split()))
        for c in range(M):
            if lst[c] == 1 : lst[c] = 0 ; Q.append((r,c,h)) # 익토 0
            elif lst[c] == 0 : lst[c] = -1 ; unripe += 1 # 덜익토 -1
            elif lst[c] == -1 : lst[c] = -2 # 빈칸 -2
        tomato.append(lst)
    box.append(tomato) # 012 , 345

print(Multi_BFS(Q,unripe))