Test = int(input())
    
for T in range(Test):
    num = int(input())
    num_plus = num
    num_lst = []
    sheep = 0

    while 1 :
        num_lst.extend(list(str(num)))
        num_lst = list(set(num_lst))
        if len(num_lst) == 10:
            break
        num += num_plus

    print(f'#{T+1} {num}') 