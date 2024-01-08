def solution(dirs):
    G = [[0] * 21 for _ in range(21)]
    r, c = 10, 10
    G[r][c] = 1
    frist = 0
    
    for d in dirs:
        if d == "U":
            rm, cm = r-1, c
            re, ce = r-2, c
        elif d == "R":
            rm, cm = r, c+1
            re, ce = r, c+2
        elif d == "D":
            rm, cm = r+1, c
            re, ce = r+2, c
        elif d == "L":
            rm, cm = r, c-1
            re, ce = r, c-2
        
        if 0 <= re < 21 and 0 <= ce < 21:
            if G[rm][cm] == 0 : 
                print(d, r, c)
                frist += 1
            G[rm][cm] = G[re][ce] = 1
            r, c = re, ce
        
#     for lst in G:
#         print(lst)
    
#     print(frist)
    return frist