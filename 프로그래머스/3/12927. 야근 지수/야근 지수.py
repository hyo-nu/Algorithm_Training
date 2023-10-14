
def solution(n, works):
    works.sort(reverse = True)
    works_len = len(works)
    
    for idx in range(1,works_len):
        if works[idx-1] != works[idx]:
            hour = (works[idx-1] - works[idx]) * idx
            print(hour,idx)
            if hour <= n :
                n -= hour
                for i in range(idx, 0, -1):
                    works[i-1] = works[i]
            
            else:
                hour = n // idx
                remain = n % idx
                
                for i in range(idx-1, -1, -1):
                    works[i] -= hour
                    if i < remain : works[i] -= 1
                break
    else:
        hour = n // works_len
        remain = n % works_len
        for i in range(works_len-1, -1, -1):
            
            works[i] -= hour
            if i < remain : works[i] -= 1
    
    result = sum([works[i]**2 if works[i] > 0 else 0 for i in range(works_len)])
    
    return result


# def noOvertime(n, works):
#     if n>=sum(works):
#         return 0;

#     while n > 0:
#         works[works.index(max(works))] -= 1
#         n -= 1

#     result = sum([w ** 2 for w in works])

#     return result