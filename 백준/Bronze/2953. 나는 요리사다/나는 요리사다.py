score_dict = {}

for i in range(1,6):
    score = list(map(int,input().split()))
    
    if i not in score_dict : score_dict[i] = sum(score)


score_lst = sorted(score_dict.items(), key = lambda x : x[1])

print(score_lst[-1][0],score_lst[-1][1])