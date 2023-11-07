def solution(elements):
    answer = 0
    
    Len_ele = len(elements)
    Set = set()
    for Length in range(1, Len_ele + 1):
        for sp in range(Len_ele):
            ep = sp + Length
            if ep < Len_ele:
                Set.add (sum(elements[sp:ep]))
            else:
                Sum = sum(elements[sp:] + elements[:ep-Len_ele])
                Set.add (Sum)
            
    return len(Set)