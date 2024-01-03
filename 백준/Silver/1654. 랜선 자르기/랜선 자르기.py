import sys

input = sys.stdin.readline
K, N = map(int,input().split())
cables = [int(input()) for _ in range(K)]

def binary_search(sp, ep):
    if sp > ep :
        return (sp + ep) // 2
    md = (sp + ep) // 2
    cnt = 0

    for cable in cables:
        cnt += cable // md

    if cnt < N:
        return  binary_search(sp, md - 1)
    elif cnt >= N:
        return  binary_search(md + 1, ep)

print(binary_search(1, max(cables)))