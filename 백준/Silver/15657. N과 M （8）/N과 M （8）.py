# 현우 코드
def DFS(n,s,lst):
    if n == M:
        ans.append(lst)
        return
    for i in range(s,N):
        DFS(n + 1, i, lst + [nums[i]])

N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

ans = []
DFS(0,0,[])
for lst in ans:
    print(*lst)