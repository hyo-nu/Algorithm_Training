# 날짜 계산기
Test = int(input())
date_dcit = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

for T in range(Test):
    start_m,start_d,end_m,end_d = map(int,input().split())
    sum_date = end_d - start_d + 1 # day만
    
    #월에 의한 day
    for m in range(start_m,end_m):
        sum_date += date_dcit[m]
        
    print(f'#{T+1} {sum_date}')
    
    