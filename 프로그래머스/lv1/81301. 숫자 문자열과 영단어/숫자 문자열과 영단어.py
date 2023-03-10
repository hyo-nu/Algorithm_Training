# 1<= s <=50
# s: zero시작하는거 x

# z,o,t,f,s,e,n

def solution(s):
    alpa_dict = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    
    num = ['0','1','2','3','4','5','6','7','8','9']
    answer = ''
    tmp = ''
    for i in s:
        tmp += i
        if tmp in alpa_dict :
            answer += alpa_dict.get(tmp)
            tmp = ''
        elif tmp in num: 
            answer += tmp
            tmp = ''
    
    return int(answer)