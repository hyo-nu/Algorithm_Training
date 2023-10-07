import bisect

N = int(input())
N_lst = sorted(list(map(int,input().split())))
M = int(input())
M_lst = list(map(int,input().split()))

for m in M_lst :
    Sum = 0
    start, end = 0, N - 1
    right = bisect.bisect_right(N_lst,m)
    left = bisect.bisect_left(N_lst,m)
    print(right-left, end = " ")