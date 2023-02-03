Test = int(input())

for c in range(Test):
    school_num = int(input())
    
    SL_list = {}
    for c in range(school_num):
        S, L = input().split()
        SL_list[S] = L

    school_lst = []
    school_score_lst = []
    
    for d in SL_list:
        school_lst.append(d)
        school_score_lst.append(int(SL_list.get(d)))
    school_score_lst.sort()
    
    for f in school_lst: 
        #print(SL_list.get(f))
        #print(school_score_lst[school_num-1])
        if int(SL_list.get(f)) == school_score_lst[school_num-1]:
            print(f)
