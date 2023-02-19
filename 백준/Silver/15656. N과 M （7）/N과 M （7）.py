# 현우 코드
def DFS(n,lst):
    if n == M:
        ans.append(lst)
        return
    for i in range(N):
        DFS(n + 1, lst + [nums[i]])

N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

ans = []
DFS(0,[])
for lst in ans:
    print(*lst)