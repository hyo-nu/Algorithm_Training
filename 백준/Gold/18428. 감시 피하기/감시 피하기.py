import sys
from itertools import combinations
input = sys.stdin.readline

def isMeet():
    global meet
    for r, c in T:
        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            for n in range(1, N):  # 각 방향으로 한칸 씩 이동
                nr, nc = r + dr * n, c + dc * n
                if 0 <= nr < N and 0 <= nc < N:  # 그래프 범위 안에 있을 때만
                    if G[nr][nc] == "O":  # 장애물 만나면
                        break  # 해당 방향 탐색 끝
                    elif G[nr][nc] == "S":  # 학생 만나면
                        return True

    meet = False
    return False

N = int(input())
G, X, T = [], [], []
for R in range(N):
    tmp = list(map(str,input().split()))
    G.append(tmp)
    for C in range(N):
        if tmp[C] == "X" : X.append((R,C))
        elif tmp[C] == "T" : T.append((R,C))

meet = True
for blocks in combinations(X,3):
    for r, c in blocks:
        G[r][c] = "O"

    if not isMeet() : break

    for r, c in blocks:
        G[r][c] = "X"

print("NO") if meet else print("YES")
