def solution(triangle):
    tri = triangle
    for R in range(1,len(tri)):
        for C in range(len(tri[R])):
            if C == 0: tri[R][C] += tri[R-1][C]
            elif C == len(tri[R])-1 : tri[R][C] += tri[R-1][C-1]
            else:
                tri[R][C] += max(tri[R-1][C-1], tri[R-1][C])
            
    return max(tri[len(tri)-1])