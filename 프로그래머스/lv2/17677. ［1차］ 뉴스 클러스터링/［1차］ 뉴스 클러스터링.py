# 11223
# 12245
# 122
# 1122345

def solution(str1, str2):
    answer = 0
    Str1 = str1.upper()
    lst1 = []
    for i in range(len(Str1)-1):
        tmp = Str1[i] + Str1[i+1]
        if tmp.isalpha():
            lst1.append(tmp)
    
    Str2 = str2.upper()
    lst2 = []
    for i in range(len(Str2)-1):
        tmp = Str2[i] + Str2[i+1]
        if tmp.isalpha():
            lst2.append(tmp)

    # 교집합 합집합
    cross = 0
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                cross += 1
                lst2[j] = -1
                break
        
    if not lst1 and not lst2:
        answer = 65536
    else:
        union = (len(lst1)+len(lst2)-cross)
        answer = int((cross/union) * 65536)
    
    return answer

