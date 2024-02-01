import sys
from collections import deque
input = sys.stdin.readline

# 맥주 1box : 20개
# 처음에 한변, 50m당 한병
# 편의점에서 빈 병 버리고, 새 맥주 구매

def BFS():
    while Q:
        sr,sc = Q.popleft()
        for nr, nc in spot:
            distance = abs(nr - sr) + abs(nc - sc)
            if distance / 50 <= 20 and (nr,nc) not in vi:
                Q.append((nr, nc))
                vi[(nr, nc)] = 1

        if (er, ec) in vi : return "happy"
    return "sad"

for test in range(int(input())):
    n = int(input()) # 편의점 수
    sr, sc = map(int, input().split()) # 집 좌표
    spot = [list(map(int,input().split())) for _ in range(n)] # 편의점 좌표
    er, ec = map(int,input().split()) # 페스티벌 좌표
    vi = {}

    spot.append([er, ec])
    Q = deque([(sr, sc)])
    vi[(sr,sc)] = 1

    print(BFS())