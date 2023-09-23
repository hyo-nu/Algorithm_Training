import sys
input = sys.stdin.readline
from collections import deque

def BFS(start, arr):
    global order
    Q = deque()
    Q.append(start)
    vi = [0] * (N + 1)
    vi[start] = 1

    while Q:
        sp = Q.popleft()
        for np in arr[sp]:
            if not vi[np]:
                Q.append(np)
                vi[np] = 1
                order += 1

N, M = map(int,input().split())
G = [[] for _ in range(N + 1)]     
G_re = [[] for _ in range(N + 1)]  

for _ in range(M):
    A,B = map(int,input().split())
    G[A].append(B)     # 학생 기준으로 점수 높은 친구들 확인용
    G_re[B].append(A)  # 학생 기준으로 점수 낮은 친구들 확인용

student = 0
for start in range(1,N + 1):  
    order = 0
    BFS(start,G)       # start라는 학생 기준으로 높은 애들 몇명인지
    BFS(start,G_re)    # start라는 학생 기준으로 낮은 애들 몇명인지

		# 그 수가 자신을 제외한 숫자가 동일 하다면 내 순위 확인이 가능
    if order == N-1 : student += 1  

print(student)