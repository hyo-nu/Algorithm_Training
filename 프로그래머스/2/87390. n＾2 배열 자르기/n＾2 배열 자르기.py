def solution(n, left, right):
    G = []
    
    for i in range(left, right + 1):
        G.append(max(i//n,i%n)+1)
            
    return G

