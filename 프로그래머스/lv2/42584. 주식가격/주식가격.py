def solution(prices):
    answer = []
    for SP in range(len(prices)):
        second = 0
        for NP in range(SP+1, len(prices)):
            second += 1
            if prices[SP] > prices[NP] : break
        answer.append(second) 
                    
    return answer