# 오늘날짜
# 유효기간 담은 terms
def days(lst):
    y,m,d = lst
    result = y * 336 + m * 28 + d
    return result

def solution(today, terms, privacies):
    term_dict = {}
    answer = []
    num = 0
    now = days(list(map(int,today.split('.'))))
    
    for term in terms:
        AL, NUM = term.split()
        term_dict.setdefault(AL,int(NUM))
    
    for p in privacies:
        num += 1
        date, al = p.split()
        pri = days(list(map(int,date.split('.'))))
        pri += term_dict.get(al) * 28 - 1
        if pri < now:
            answer.append(num)
    
    return answer