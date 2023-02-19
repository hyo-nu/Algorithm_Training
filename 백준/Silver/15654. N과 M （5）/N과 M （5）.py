# 현우 코드
def DFS(n,lst):
    if n == M:
        return ans.append(lst)

    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            DFS(n + 1, lst + [nums[i]])
            v[i] = 0
N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

ans = []
v = [0] * (N+1)
DFS(0,[])
for lst in ans:
    print(*lst)