# 현우 코드
def DFS(n,lst):
    if n == M:
        return ans.append(lst)

    for i in range(1,N+1):
        if n == 0:
            DFS(n + 1, lst + [i])

        elif lst[n-1] <= i:
            DFS(n + 1, lst + [i])

N,M = map(int,input().split())
ans = []
DFS(0,[])
for lst in ans:
    print(*lst)