import sys
input = sys.stdin.readline

N, M = map(int,input().split())
_, *knows = map(int,input().split())
G = [[0] * (N+1) for _ in range(M)]
count = 0

for round in range(M):
    cnt, *party = map(int,input().split())
    truth = False

    for num in party:
        if num not in knows : G[round][num] = 1
        else :
            truth = True

    if truth :
        def goback(round):
            for num in range(1, N+1):
                if G[round][num] :
                    G[round][num] = 0
                    knows.append(num)
                    for i in range(M):
                        if G[i][num] : goback(i)
        goback(round)

for lst in G:
    if sum(lst) > 0 : count += 1

print(count)