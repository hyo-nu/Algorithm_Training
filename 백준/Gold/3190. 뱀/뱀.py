from collections import deque

N = int(input())
G = [[0] * N for _ in range(N)]

for _ in range(int(input())):
    r, c = map(int,input().split())
    G[r-1][c-1] = 1

turn = [list(map(str,input().split())) for _ in range(int(input()))]

dr = [0, 1, 0, -1] # 우 하 좌 상
dc = [1, 0, -1, 0]
snake = deque([(0,0)])
turn = deque(turn)
time = d = 0

while turn:
    move, dire = turn.popleft()
    move = int(move) - time
    for _ in range(move):
        r, c = snake[-1][0], snake[-1][1] # 이전 뱀 머리 위치
        nr, nc = r + dr[d], c + dc[d]     # 현재 뱀 머리 위치
        snake.append((nr,nc))
        G[r][c] = 2
        time += 1
        if nr < 0 or nr >= N or nc < 0 or nc >= N or G[nr][nc] == 2:
            break
        # 사과가 없을 때
        if G[nr][nc] == 0 :
            br, bc = snake.popleft()
            G[br][bc] = 0

    if dire == "D" : d = ( d + 1 ) % 4
    else : d = ( d + 3 ) % 4
    if nr < 0 or nr >= N or nc < 0 or nc >= N or G[nr][nc] == 2:
        break

while not turn:
    if nr < 0 or nr >= N or nc < 0 or nc >= N or G[nr][nc] == 2:
        break
    r, c = snake[-1][0], snake[-1][1]  # 이전 뱀 머리 위치
    nr, nc = r + dr[d], c + dc[d]  # 현재 뱀 머리 위치
    snake.append((nr, nc))
    G[r][c] = 2
    time += 1
    # 사과가 없을 때
    if G[nr][nc] == 0:
        br, bc = snake.popleft()
        G[br][bc] = 0

print(time)