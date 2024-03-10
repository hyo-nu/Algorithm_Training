import sys;
input = sys.stdin.readline

def min_Init(node, start, end):
    mid = (start + end) // 2
    if start == end :
        min_tree[node] = nums[start]
        return min_tree[node]
    min_tree[node] = min(min_Init(node*2,start,mid),min_Init(node*2+1,mid+1,end))
    return min_tree[node]

def max_Init(node, start, end):
    mid = (start + end) // 2
    if start == end:
        max_tree[node] = nums[start]
        return max_tree[node]
    max_tree[node] = max(max_Init(node*2, start, mid),max_Init(node*2+1,mid+1,end))
    return max_tree[node]

def Min(node,start,end,left,right):
    mid = (start + end) // 2
    if left > end or right < start:
        return 1000000000001
    if left <= start and right >= end:
        return min_tree[node]
    k1 = Min(node*2, start, mid, left, right)
    k2 = Min(node*2+1, mid + 1, end, left, right)
    return min(k1,k2)

def Max(node, start, end, left, right):
    mid = (start + end) // 2
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return max_tree[node]
    k1 = Max(node*2, start,mid,left,right)
    k2 = Max(node*2+1, mid + 1,end,left,right)
    return max(k1,k2)

n,m = map(int,input().split())
nums = [int(input()) for _ in range(n)]
min_tree = [0] * (4 * n)
max_tree = [0] * (4 * n)

min_Init(1,0,n-1)
max_Init(1,0,n-1)

for _ in range(m):
    a, b = map(int,input().split())
    print(Min(1,0,n-1,a-1,b-1),end = " ")
    print(Max(1,0,n-1,a-1,b-1))