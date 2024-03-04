import sys;
input = sys.stdin.readline

def Init(node,start,end):
    mid = (start + end) // 2
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    tree[node] = min(Init(node*2, start, mid), Init(node*2+1, mid+1, end))
    return tree[node]

def Min(node, start, end, left, right):
    mid = (start + end) // 2
    if left > end or right < start:
        return 10000000001
    if left <= start and right >= end:
        return tree[node]
    k1 = Min(node*2, start, mid, left, right)
    k2 = Min(node*2 + 1, mid+1, end, left, right)
    return min(k1, k2)

n, m = map(int,input().split())
nums = [int(input()) for i in range(n)]
tree = [0] * (4 * n)

Init(1,0,n-1)
for i in range(m):
    a, b = map(int,input().split())
    print(Min(1, 0, n - 1, a - 1, b - 1))