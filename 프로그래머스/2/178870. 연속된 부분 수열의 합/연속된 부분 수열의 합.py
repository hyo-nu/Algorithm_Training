def solution(sequence, k):
    N = len(sequence)
    sp = ep = N - 1
    value = 0
    
    while sp >= 0 and ep >= 0:
        if value < k :
            value += sequence[sp]
            sp -= 1
        
        elif value > k:
            value -= sequence[ep]
            ep -= 1
        
        elif value == k:
            if sp < 0 : break
            if sequence[sp] != sequence[ep] : break
            else : sp -= 1 ; ep -= 1
    
    
    return [sp+1,ep]