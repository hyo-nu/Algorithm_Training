from itertools import combinations
import math

def solution(clothes):
    cloth_dict = {}
    
    for cloth, kind in clothes:
        cloth_dict[kind] = cloth_dict.get(kind, 0) + 1
    
    cloth_cnt = [ cnt for cnt in cloth_dict.values()]
    
    result = 1
    
    for cnt in cloth_dict.values():
        result *= (cnt + 1)
            
    return result - 1

