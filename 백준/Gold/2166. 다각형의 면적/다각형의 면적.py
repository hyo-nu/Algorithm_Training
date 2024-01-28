import sys
input = sys.stdin.readline

N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]
G.append(G[0])

a = b = 0
for i in range(N):
    a += G[i][0] * G[i+1][1]
    b += G[i][1] * G[i+1][0]

print(round(abs((a-b)/2),1))