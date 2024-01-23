from collections import deque

def solution(n, wires):
    answer = n-1
    
    for ev1, ev2 in wires:
        G = [[] for _ in range(n+1)]
        for v1, v2 in  wires:
            if ev1 != v1 or ev2 != v2:
                G[v1].append(v2)
                G[v2].append(v1)
        
        vi = [0] * (n + 1)
        tmp = []
        for sp in range(1,n + 1):
            Q = deque([sp])
            vi[sp] = 1
            network = 1
            while Q:
                Now = Q.popleft()
                for Next in G[Now]:
                    if not vi[Next]:
                        Q.append(Next)
                        vi[Next] = 1
                        network += 1
            tmp.append(network)
        tmp.sort(reverse = True)
        answer = min(answer, tmp[0]-tmp[1])
    return answer