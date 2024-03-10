def solution(triangle):
    tri = triangle
    
    result = 0
    for r in range(1, len(tri)):
        for c in range(r + 1):
            Max = 0
            if c-1 >= 0 : Max = max(Max,tri[r-1][c-1])
            if c < r : Max = max(Max,tri[r-1][c])
            tri[r][c] += Max
            result = max(result,tri[r][c])
    
    return result

# def solution(triangle):
#     tri = triangle
#     for R in range(1,len(tri)):
#         for C in range(len(tri[R])):
#             if C == 0: tri[R][C] += tri[R-1][C]
#             elif C == len(tri[R])-1 : tri[R][C] += tri[R-1][C-1]
#             else:
#                 tri[R][C] += max(tri[R-1][C-1], tri[R-1][C])
            
#     return max(tri[len(tri)-1])