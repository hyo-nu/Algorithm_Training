import sys
input = sys.stdin.readline

N, L = map(int,input().split())

spot = time = 0
for i in range(N):
    D, R, G = map(int,input().split())
    spot, time = D, time + (D - spot)

    if time % (R + G) <= R: # 빨간불 케이스
        time += (R - time % (R + G))

time += (L - spot)
print(time)