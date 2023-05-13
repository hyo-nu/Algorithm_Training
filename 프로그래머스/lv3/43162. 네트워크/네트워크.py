def solution(n, computers):
    vi = [0] * (n + 1)
    net = 0
    
    def DFS(v):
        vi[v] = 1
        S = [v]
        while S:
            for w in range(1,n+1):
                if v != w and computers[v-1][w-1] == 1:
                    if not vi[w]:
                        vi[w] = 1
                        S.append(v)
                        v = w
                        break
            else : v = S.pop()
        return 1
        
    for v in range(1,n + 1):
        if not vi[v]:    
            net += DFS(v)
            
    return net
            