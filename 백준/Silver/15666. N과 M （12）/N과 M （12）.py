# 현우 코드
def DFS(n,s,lst):
    if n == M:
        ans.append(lst)
        return

    for j in range(s,len(num)):# 0 1 2
        DFS(n+1, j, lst + [num[j]])

N,M = map(int,input().split())
nums = list(map(int,input().split()))
num = list(set(nums))
num.sort()

ans = []
DFS(0,0,[])
for lst in ans:
    print(*lst)