from collections import deque

# N 크기 만큼 G 만들기
N = int(input())
G = [[0] * N for _ in range(N)]

# 사과의 위치 표시하기
for _ in range(int(input())):
    r, c = map(int,input().split())
    G[r-1][c-1] = 1

def snakeMove():
    global time, stop, d
    r, c = snake[-1][0], snake[-1][1] # 현재 뱀 머리 위치
    nr, nc = r + dr[d], c + dc[d]     # 다음 뱀 머리 위치
    snake.append((nr, nc))            # 다음 뱀 머리 위치 담기
    G[r][c] = 2                       # 현재 뱀 꼬리 표시
    time += 1                         # 1초 으흠

    # 뱀이 벽 or 자기 몸에 부딫히면 stop
    if nr < 0 or nr >= N or nc < 0 or nc >= N or G[nr][nc] == 2:
        stop = 1
        return

    # 이동 위치에 사과가 없을 때
    if G[nr][nc] == 0:
        br, bc = snake.popleft() # 꼬리를 잘라서
        G[br][bc] = 0            # G에는 0으로 표시한다.

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]     # 우 하 좌 상
snake = deque([(0,0)]) # 뱀 시작위치
time = stop = d = 0    # 총 시간, 뱀 방향

for _ in range(int(input())):
    move, dire = map(str,input().split())
    move = int(move) - time
    for _ in range(move):
        snakeMove()
        if stop == 1: break
    if stop == 1 : break

    # 방향 전환
    if dire == "D" : d = ( d + 1 ) % 4
    else : d = ( d + 3 ) % 4

# 방향 전환 정보를 다 체크했는데도 게임이 안 끝났을 때
while stop == 0:
    snakeMove()

print(time)