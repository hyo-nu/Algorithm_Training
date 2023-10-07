def binary_search(start,end,target):
    while start <= end :
        mid = (start + end) // 2

        if target == N_lst[mid]:
            return 1
        elif target > N_lst[mid]:
            start = mid + 1
        elif target < N_lst[mid]:
            end = mid - 1

    return 0

N = int(input())
N_lst = sorted(list(map(int,input().split())))
M = int(input())
M_lst = list(map(int,input().split()))

for m in M_lst :
    start, end = 0, N - 1
    print(binary_search(start, end, m))

