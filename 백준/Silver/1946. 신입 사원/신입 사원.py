import sys;
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    lst.sort()

    num, cnt = lst[0][1], 1
    for i in range(1,N):
        if lst[i][1] < num :
            cnt += 1 ;
            num = lst[i][1]

    print(cnt)