num = int(input())

for n in range(1,num+1):
    n_lst = list(str(n)) # 숫자를 나눠서 보기위함

    count3 = 0 # 각 자릿수의 3의 배수의 갯수 새기
    for nn in n_lst:
        if int(nn) % 3 == 0 and int(nn) != 0 : count3 += 1
        
    if count3 == 0 : print(n,end = '') # 3,6,9 제외하고 숫자3이 들어가지 않는 3의배수

    else: 
        for c in range(count3):
            print('-',end = '') # 숫자3의 갯수 만큼 '-'출력하자 

    print('',end = ' ')

   
    
    
    
    
