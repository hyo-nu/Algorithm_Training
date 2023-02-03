Test = int(input())

for T in range(Test):
    num = int(input())
    next = 0

    result = []
    for n in range(num):
        alph, cnt = input().split()
        
        for c in range(int(cnt)):
            result.append(alph)
    print(f'#{T+1}')

    for r in range(1,len(result)+1):
        
        if r % 10 == 0 : print(result[r-1] , end = '') ; print()
        else : print(result[r-1] , end = '')
    print()          