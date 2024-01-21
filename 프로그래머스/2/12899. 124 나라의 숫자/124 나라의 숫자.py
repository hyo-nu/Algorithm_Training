def solution(n):
    num = ""
    minus = 0
    while n + minus:
        n += minus
        if n % 3 :
            num += str(n % 3)
            minus = 0
        else :
            num += "4"
            minus = -1
        n //= 3
    
    return num[::-1]