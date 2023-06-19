def solution(routes):
    G = [0] * 60001
    result = 0
    routes.sort(key = lambda x : x[1])
    
    for SP, EP in routes:
        if 1 not in G[SP + 30000 : EP + 30001]:   

            G[SP + 30000 : EP + 30001] = [1] * (EP-SP+1)
            result += 1
    return result