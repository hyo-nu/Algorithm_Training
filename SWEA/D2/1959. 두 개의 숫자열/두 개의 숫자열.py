Test = int(input())

def list_mul(A_lst,B_lst):
       
    if len(A_lst) < len(B_lst) :
        A_lst, B_lst = B_lst, A_lst     
      
    sum_lst = []
    
    for AB in range(len(A_lst)-len(B_lst)+1):
        sums = 0
        for B in range(len(B_lst)):
            sums += A_lst[AB + B] * B_lst[B]
        sum_lst.append(sums)          
    return sum_lst

for T in range(Test):
    A , B = map(int,input().split())
    A_lst = list(map(int,input().split()))
    B_lst = list(map(int,input().split()))
    sums_lst = list_mul(A_lst,B_lst)
    sums_lst.sort()
    print(f'#{T+1} {sums_lst[-1]}')

    # if len(A) > len(B)
    
    # if N < M : 