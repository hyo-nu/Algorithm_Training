# 스테이지 도달 but 클리어 실패 수 / 스테이지 도달 수

# 스테이지수 1<=N<=500
#  1<= 스테이지 길이 <=200,000
def solution(N, stages):
    
    percent_lst = []
    answer = []
    for i in range(1,N+1):
        total = retire = 0
        for j in stages:
            
            if j >= i : total += 1
            if j == i : retire += 1
        try:      
            percent_lst.append([i,retire/total])
        except: percent_lst.append([i,0])
    percent_lst.sort(key = lambda x : x[1],reverse = True)
    
    for num,per in percent_lst:
        answer.append(num)
    
    return answer