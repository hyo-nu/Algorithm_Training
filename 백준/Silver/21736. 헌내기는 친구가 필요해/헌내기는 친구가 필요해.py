import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
campus = []
doyeon = deque()

for r in range(N):
    tmp = list("X"+input().rstrip()+"X")
    campus.append(tmp)
    for c in range(M+2):
        if tmp[c] == "I":
            tmp[c] = "X"
            doyeon.append((r+1,c))

campus = [["X"] * (M+2)] + campus + [["X"] * (M+2)]

meet = 0
while doyeon:
    r, c = doyeon.popleft()
    for dr, dc in ((-1,0),(0,1),(1,0),(0,-1)):
        nr, nc = r + dr, c + dc
        if campus[nr][nc] != "X":
            doyeon.append((nr,nc))
            if campus[nr][nc] == "P" : meet += 1
            campus[nr][nc] = "X"

print(meet if meet else "TT")