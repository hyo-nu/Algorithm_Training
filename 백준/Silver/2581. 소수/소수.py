

decimal_lst = []
M = int(input())
N = int(input())

for mn in range(M,N+1):
   
    check = 0
    for c in range(1,mn+1):
        if mn % c == 0:
            check += 1
    if check == 2:
        decimal_lst.append(mn)

if len(decimal_lst) == 0: 
    print(-1)

else :
    print(sum(decimal_lst))
    print(decimal_lst[0])