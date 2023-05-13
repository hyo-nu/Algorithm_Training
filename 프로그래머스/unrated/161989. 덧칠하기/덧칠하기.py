def solution(n, m, section):
    
    SP = paint = area = 0

    while SP <= len(section)-1:
        if area <= section[SP]:
            paint += 1
            area = section[SP] + m
        SP += 1
        
    return paint