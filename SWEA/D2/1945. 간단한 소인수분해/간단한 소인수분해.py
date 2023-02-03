Test = int(input())

prime_lst = [2,3,5,7,11]    
for T in range(Test):
    num = int(input())
    print(f'#{T+1}',end = ' ')
    
    for p in prime_lst:
        count = 0
        while num % p == 0:
            count += 1
            num = num // p
        print(count , end = ' ')
    print()
    