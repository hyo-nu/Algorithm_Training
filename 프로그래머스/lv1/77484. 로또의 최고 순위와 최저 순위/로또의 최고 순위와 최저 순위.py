def solution(lottos, win_nums):
    

    Min = zero = 0
    rank_lst = {6:1 , 5:2 , 4:3 , 3:4 , 2:5}
    for i in lottos:
        if i in win_nums:Min += 1
        if i == 0 : zero += 1
    Max = Min + zero
    answer = [rank_lst.get(Max,6),rank_lst.get(Min,6)]
    
    
    return answer