import sys;
input = sys.stdin.readline

def Init(node, start, end):
    mid = (start + end) // 2
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    tree[node] = Init(node*2, start, mid) + Init(node*2+1,mid+1,end)
    return tree[node]

def update(node,start,end,idx,val):
    mid = (start + end) // 2
    if start == end == idx :
        tree[node] = val
        return
    if idx < start or end < idx:
        return
    update(node*2, start, mid, idx, val)
    update(node*2+1, mid+1, end,idx, val)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def Sum(node, start, end, left, right):
    mid = (start + end) // 2
    if left > end or right < start :
        return 0
    if left <= start and right >= end:
        return tree[node]
    k1 = Sum(node*2, start, mid, left, right)
    k2 = Sum(node*2+1, mid+1, end, left, right)
    return k1 + k2

N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
tree = [0] * (4 * N)

Init(1,0,N-1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1 : update(1, 0, N-1,b-1, c)
    else : print(Sum(1, 0, N-1, b-1,c-1))