# 대문자 -> 소문자
# 알파벳,숫자,-,_,. 제외하고 제거
# . 연속 두번이상이면 하나로 치환
# . 처음or끝이면 제거
# 빈문자열이면 a 삽입
# 16자 이상이면 뒤에 제거
# 제거 후 . 끝이면제거
# 2자 이하면은 마지막문자 추가 3일 때까지

def solution(new_id):
    s = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-','_','.','0','1','2','3','4','5','6','7','8','9']
    tmp = ''
    answer = []
    for i in new_id:
        if i.lower() in s: tmp += i.lower()

    if len(tmp)>=2:
        for i in range(len(tmp) - 1):
            if tmp[i] == '.':
                if tmp[i + 1] != '.': answer.append(tmp[i])
            else:answer.append(tmp[i])

    answer.append(tmp[-1])
    if answer:
        if answer[0] == '.': answer.pop(0)
    if answer:
        if answer[-1] == '.': answer.pop()
        
    if not answer: answer.append('a')
    answer = answer[:15]

    if answer[len(answer) - 1] == '.': answer.pop()
    while len(answer) <= 2:
        answer += answer[-1]
    answer = ''.join(answer)
    return answer