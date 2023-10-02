def binary_search(start,end):
    if start > end:
        return (start + end) // 2
    mid = (start + end) // 2
    Sum = 0

    for i in range(N-1,-1,-1):
        if tree[i] > mid : Sum += tree[i] - mid
        else: break

    if Sum == M:
        return mid
    elif Sum < M :
        return binary_search(start, mid - 1)
    elif Sum > M :
        return binary_search(mid + 1, end)

N, M = map(int,input().split())
tree = sorted(list(map(int,input().split())))

start, end = 0, tree[N-1]
result = binary_search(start,end)

print(result)