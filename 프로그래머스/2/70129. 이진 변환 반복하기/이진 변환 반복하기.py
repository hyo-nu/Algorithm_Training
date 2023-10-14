def solution(s):
    
    change = zero= 0
    
    while s != "1":
        one = s.count("1")
        zero += len(s) - one
        s = format(one,"b")
        change += 1

    return [change, zero]