Test = int(input())
date_dict = {'01' : 31, '02' : 28, '03' : 31,
            '04' : 30, '05' : 31, '06' : 30,
            '07' : 31, '08' : 31, '09' : 30,
            '10' : 31, '11' : 30, '12' : 31}

for T in range(Test):
    date = input() 
    # month check
    if 1 <= int(date[4:6]) <= 12:
        #day check
        if date[4:6] in date_dict.keys():
            if 1 <= int(date[6:]) <= date_dict.get(date[4:6]):
                print(f'#{T+1} {date[:4]}/{date[4:6]}/{date[6:]}')
            else:
                print(f'#{T+1} -1')
    else:
        print(f'#{T+1} -1') 