Test = int(input())


for T in range(Test):
    n_lst = [1]
    N = int(input())
    print(f'#{T+1}') 
     
    for n in range(N):      
        for p in n_lst:
            print(p,end = ' ')
        print()
        
        if n == 0 : n_lst.append(1)
        else :
            n_lst_copy = []
            for i in n_lst : n_lst_copy.append(i)
            
            n_lst = [1,1]
            for j in range(len(n_lst_copy)-1):
                n_lst.insert(j+1,n_lst_copy[j] + n_lst_copy[j+1])

            