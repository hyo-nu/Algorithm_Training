import sys
input = sys.stdin.readline

N = int(input())
size = [list(map(int,input().split())) for i in range(N)]

for i in range(N):
    order = 1
    for j in range(N):
        if i != j:
            if size[i][0] < size[j][0] and size[i][1] < size[j][1]:
                order += 1
    print(order,end = " ")
    