import sys;
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    lst = [0, 1]
    cnt = 2
    Sum = 0
    result = []

    while (True):
        if lst[cnt-1] + lst[cnt-2] > N : break
        lst.append(lst[cnt-1] + lst[cnt-2])
        cnt += 1
    for i in range(cnt-1,-1,-1):
        if Sum == N : break
        if Sum + lst[i] <= N :
            Sum += lst[i]
            result.append(lst[i])
    print(*result[::-1])