import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

preorder = []
while True:
    try : preorder.append(int(input()))
    except : break

def post(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if preorder[i] > preorder[start]:
            mid = i
            break
    post(start + 1, mid - 1) # 왼쪽트리
    post(mid, end)           # 오른쪽트리
    print(preorder[start])

post(0,len(preorder) - 1)