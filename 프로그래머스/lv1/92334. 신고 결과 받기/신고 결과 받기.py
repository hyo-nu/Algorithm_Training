def solution(id_list, report, k):
    ID_dict = {}
    L = len(id_list)
    call = [[0] * L for _ in range(L)]
    
    for i in range(L):
        ID_dict.setdefault(id_list[i],i)
        
    for FT in report:
        F,T = FT.split()
        call[ID_dict[T]][ID_dict[F]] = 1 
    
    result = [0] * L
    
    for num,x in enumerate(id_list,start=1):
        print(num,x)
    
    
    for lst in call:
        if lst.count(1) >= k:
            for i in range(L):
                if lst[i] == 1:
                    result[i] +=1    
    return result