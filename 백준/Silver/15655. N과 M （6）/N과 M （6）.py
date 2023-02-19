# 현우 코드
def DFS(n,lst):
    if n >= N:
        if len(lst) == M:
            ans.append(lst)
        return
    DFS(n + 1, lst + [nums[n]])
    DFS(n + 1, lst)

N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

ans = []
DFS(0,[])
for lst in ans:
    print(*lst)