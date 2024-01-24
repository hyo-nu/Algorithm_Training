from collections import deque

def solution(storey):
    button = 0
    while storey:
        quotient = storey // 10
        remainder = storey % 10
        
        if remainder < 5 : 
            storey = quotient
            button += remainder
        
        elif remainder > 5 : 
            storey = quotient + 1
            button += 10 - remainder
        
        elif remainder == 5 :
            if quotient % 10 < 5: 
                storey = quotient
                button += remainder
            else :
                storey = quotient + 1
                button += 10 - remainder
        
    return button


