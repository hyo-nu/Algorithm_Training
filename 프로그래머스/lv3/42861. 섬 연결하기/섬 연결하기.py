def solution(n, costs):
    costs.sort(key = lambda x : x[2])
    rep = [i for i in range(n)]
    
    def find_set(x):
        while x != rep[x]:
            x = rep[x]
        return x
    
    def union(x,y):
        rep[find_set(y)] = find_set(x)        
          
    MST = []
    Sum = cnt = 0
    for u, v, weight in costs:
        if find_set(u) != find_set(v):
            cnt += 1
            Sum += weight
            MST.append([u,v,weight])
            union(u,v)
            if cnt == n - 1 : break
    
    return Sum
