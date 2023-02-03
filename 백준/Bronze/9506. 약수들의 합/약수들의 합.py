
while True:
    n = int(input())
    
    if n == -1: # while문 종료
        break
    
    n_lst = []
    for c in range(1,n):
        if n % c == 0:
            n_lst.append(c)
           
    if sum(n_lst) == n: # 완전수 판별문
        print(f'{n} = ',end = '')
        for d in range(len(n_lst)):
            print(n_lst[d],end = '')
            if d != len(n_lst)-1:
                print(' + ', end = '')          
        print()
    else :
        print(f'{n} is NOT perfect.')
    
 