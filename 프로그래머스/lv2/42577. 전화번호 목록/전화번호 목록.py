def solution(phone_book):
    PB, L = sorted(phone_book), len(phone_book)
    
    for i in range(L-1):
        if PB[i] in PB[i+1][:len(PB[i])] : return False
    return True
    
    # PB, L = phone_book,len(phone_book)
    #    for i in range(L-1):
    #         for j in range(i+1,L):
    #            if PB[j] in PB[i] : return False
    #            if PB[i] in PB[j] : return False
    #    return True
             