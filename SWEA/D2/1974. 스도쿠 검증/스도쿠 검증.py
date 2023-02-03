Test = int(input())

for T in range(Test):
    check_cnt = 0
    row_check = {}
    box_check = {}
    
    for c in range(9):
        sudocu = list(map(int,input().split()))
        
        # 가로줄 먼저 확인
        sudocu_sort = set(sudocu)
        if len(sudocu) != len(sudocu_sort) : check_cnt += 1

        # 세로줄 딕셔너리
        for sdc in range(len(sudocu)):
            if sdc not in row_check : row_check[sdc] = [sudocu[sdc]]
            else : row_check[sdc] = row_check[sdc] + [sudocu[sdc]]
         
        # box 딕셔너리
        a = c // 3
        for b in range(3):
            for c in range(3):
                if (3*a+b) not in box_check : box_check[3*a+b] = [sudocu[3*b+c]]
                else : box_check[3*a+b] =box_check[3*a+b] + [sudocu[3*b+c]]
        
    for d in range(9):
        if len(row_check.get(d)) != len(set(row_check.get(d))): check_cnt += 1

        if len(box_check.get(d)) != len(set(box_check.get(d))): check_cnt += 1

    if check_cnt == 0: print(f'#{T+1} 1')
    else : print(f'#{T+1} 0')
