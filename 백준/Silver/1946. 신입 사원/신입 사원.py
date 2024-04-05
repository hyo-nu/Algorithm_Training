import sys;
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    lst.sort(key = lambda x : -x[0])

    num, cnt = 1000000, 0
    for i in range(N-1,-1,-1):
        if lst[i][1] < num :
            cnt += 1
            num = lst[i][1]

    print(cnt)