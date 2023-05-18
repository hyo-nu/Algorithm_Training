def solution(msg):
    dic = {chr(64 + i) : i for i in range(1,27)}
    SP = 0
    add = 27
    result = []
    while len(msg)-1 >= SP:
        tmp = 1
        while True:
            if SP+tmp <= len(msg) and msg[SP:SP+tmp] in dic:
                tmp += 1
            else:
                tmp -= 1
                break
            
        result.append(dic[msg[SP:SP+tmp]])
        dic[msg[SP:SP+tmp+1]] = add
        SP, add = SP + tmp, add + 1
    
    return result