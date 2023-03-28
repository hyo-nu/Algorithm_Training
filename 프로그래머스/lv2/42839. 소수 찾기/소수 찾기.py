from itertools import permutations

def solution(numbers):
    N = len(numbers) # 7
    lst = []
    sosu = 0
    
    tmp = []
    for i in range(1,N+1): # 1,2,3,4,5,6,7
        num_lst = list((permutations(numbers,i)))
        
        lst.extend([int(''.join(list(num))) for num in num_lst])  
        lst = list(set(lst))
    for n in lst:
        check = 2
        print(n)
        if n != 1 and n != 0:
            for i in range(2,n):
                if n % i == 0:
                    check +=1
                    break
            if check == 2:
                sosu += 1
                print(n)
    return sosu
    

            
