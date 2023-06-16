def solution(sizes):
    
    Max_W = Max_H = 0
    for W,H in sizes:
        if W < H : W,H = H, W
        if Max_W < W : Max_W = W
        if Max_H < H : Max_H = H
    
    return Max_W * Max_H